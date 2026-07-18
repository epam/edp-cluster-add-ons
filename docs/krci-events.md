# krci-events: Defining and Extending Platform Notifications

> Interim location — this guide's final home is docs.kuberocketci.io.

The `krci-events` add-on is the routing layer of the KubeRocketCI notification bus. It sits
on top of the `argo-events` add-on (engine: controller, CRDs, JetStream EventBus) and turns
platform events into notifications delivered to the KRCI portal, Microsoft Teams, and other
channels. All configuration is Helm values — you never author Sensor manifests by hand.

## Model

```
eventTypes    WHAT  — match an event (Ce-Type + payload filters) and extract canonical
                      notification fields (type, severity, title, body, link, facts) from
                      the event body via Sprig templates
destinations  WHERE — one entry = one delivery endpoint = one generated Sensor (one pod);
                      each destination picks the eventTypes it wants via `routes`
```

Destinations never see event body shapes — only the canonical fields a route extracts.
`*Template` values are Sprig templates rendered by Argo Events at delivery time against
`{{ .Input.header }}` / `{{ .Input.body }}` (not by Helm).

## Add a new event type

Example: notify on failed autotests pipelines.

```yaml
eventTypes:
  autotests-failed:
    source: { eventSourceName: tekton-events, eventName: tekton }
    ceType: dev.tekton.event.pipelinerun.failed.v1
    matchData:
      - path: body.pipelineRun.metadata.labels.app\.edp\.epam\.com/pipelinetype
        value: autotests
    notification:
      type: autotests.failed
      severity: warning
      idTemplate: "{{ .Input.body.pipelineRun.metadata.uid }}"
      namespaceTemplate: "{{ .Input.body.pipelineRun.metadata.namespace }}"
      titleTemplate: "Autotests failed: {{ .Input.body.pipelineRun.metadata.name }}"
      bodyTemplate: "..."
      linkTemplate: "/c/core/cicd/pipelineruns/{{ .Input.body.pipelineRun.metadata.namespace }}/{{ .Input.body.pipelineRun.metadata.name }}"
      buttonLinkKind: pipelineUrl
      buttonTitle: Open PipelineRun
      facts:
        - { title: PipelineRun, valueTemplate: "{{ .Input.body.pipelineRun.metadata.name }}" }

destinations:
  msteams:
    routes: [build-failed, deploy-failed, autotests-failed]   # opt in per destination
```

No new pods: existing destination Sensors roll with the added dependency/trigger.

## Add a destination (e.g. a second Teams channel)

```yaml
destinations:
  msteams-quality:
    enabled: true
    kind: msteams-card
    webhookUrl: ""            # this channel's Power Automate Workflows webhook (see Secrets)
    linkFallbackUrl: https://<portal-host>
    routes: [autotests-failed]
    retryStrategy: { steps: 5, duration: 10s }
```

Each destination generates its own Sensor (`notify-msteams-quality`) — isolated pod, own
routing policy, own Argo CD health. Adding a new destination *kind* (e.g. Slack) is a
one-time platform change: a payload partial in `templates/_helpers.tpl`.

## Custom producers (non-Tekton events)

Any component can publish by POSTing a CloudEvents-shaped HTTP request to an EventSource
endpoint:

```
POST http://tekton-events-eventsource-svc.<ns>.svc:12000/<endpoint>
Ce-Id: <unique id — becomes the portal dedup key>
Ce-Type: com.epam.krci.<domain>.<event>.v1
Ce-Time: <RFC3339>
Content-Type: application/json

{ ...producer-defined body... }
```

Then add an `eventTypes` entry whose templates extract fields from *that* body. Patterns:

- **Domain event (recommended)**: producer emits a typed event (e.g.
  `com.epam.krci.sonarqube.qualitygate.failed.v1`); one route per type; subscribable in the
  portal by `notification.type`.
- **Third-party webhook direct**: point a tool's native webhook (e.g. SonarQube) at an
  endpoint and use `matchData` on body fields instead of `ceType`. No code, but you accept
  the tool's payload shape and retry semantics.
- **Thresholds/stateful conditions** (queue depth > N): detect the *crossing* in the
  producer (operator reconcile loop) and emit one discrete event. Do not encode state
  machines in Sensor filters — the bus is edge-triggered and will re-fire on every update.

## Rules that keep delivery robust

1. **Never use `dataKey` for optional fields** — a missing key aborts the trigger with no
   fallback. Use `dataTemplate` with an explicit default (the generator does this for all
   built-in fields; timestamps fall back to `now`).
2. **`Ce-Id` is the idempotency key** — the portal ignores redeliveries of the same id;
   chat channels have no dedup, so producers must send stable ids.
3. **Links**: `linkTemplate` is the portal-relative path; card buttons use
   `buttonLinkKind: pipelineUrl` (resolves the Tekton `pipelineUrl` param convention,
   falling back to `linkFallbackUrl`) or `buttonLinkKind: template` + `buttonLinkTemplate`.
4. **Label keys with dots** must be gjson-escaped in `matchData` paths:
   `labels.app\.edp\.epam\.com/pipelinetype`.
5. A trigger references only its own route's dependency — enforced by the generator
   (cross-referencing crashes the sensor pod in Argo Events v1.9).

## Secrets

- **Portal token**: Secret `portal-events-token` (this namespace) + the same value as
  `INTERNAL_EVENTS_TOKEN` in the portal deployment.
- **Teams webhook URLs embed their credential** (`sig` query param) and Argo Events cannot
  read the HTTP trigger URL from a Secret (upstream limitation). Supply `webhookUrl` from a
  private values source (SOPS overlay) or patch the deployed Sensor. Create Workflows
  webhooks under a service account with co-owners (owner-leaves = orphaned flow), send the
  wrapped `type: message` + Adaptive Card envelope only, and treat the URL as rotatable —
  Microsoft has changed the URL scheme twice since 2024.

## Testing

Render-time: `helm template` fails on routes referencing undefined eventTypes.
Runtime smoke test — POST a synthetic event and watch the sensor logs:

```bash
kubectl run curl-test -i --rm --restart=Never -n argo-events \
  --image=curlimages/curl:8.9.1 --command -- sh -c \
  'curl -s -X POST -H "Content-Type: application/json" \
     -H "Ce-Id: smoke-$(date +%s)" -H "Ce-Type: dev.tekton.event.pipelinerun.failed.v1" \
     -H "Ce-Source: /smoke" -H "Ce-Specversion: 1.0" \
     -d "{\"pipelineRun\":{\"metadata\":{\"name\":\"smoke\",\"namespace\":\"krci\",\"uid\":\"smoke-1\",\"labels\":{\"app.edp.epam.com/pipelinetype\":\"build\"}}}}" \
     http://tekton-events-eventsource-svc:12000/tekton'
kubectl logs -n argo-events deploy -l sensor-name=notify-msteams | grep "Successfully processed"
```

Note: "Successfully processed" confirms the HTTP call was made, not that the channel
accepted it — Teams delivery problems (bad URL, malformed card) do not surface as sensor
errors. Verify the channel end for functional checks.
