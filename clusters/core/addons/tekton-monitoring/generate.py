#!/usr/bin/env python3
"""Generate Tekton analytics dashboards D2-D6 (+ fix D1 panel 7) for Grafana sidecar."""
import json, os

# Emit next to this script, into the chart's files/ directory — templates/grafana-dashboards.yaml
# loads each JSON verbatim via .Files.Get, so regenerating here is all that is needed.
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

# uid of the kube-prometheus-stack Prometheus datasource. The stack provisions it with
# uid "prometheus" by default; override here if grafana.sidecar.datasources.uid changes.
DS = {"type": "prometheus", "uid": "prometheus"}

# ---- query helpers -------------------------------------------------------
# These counters reset on controller restart and gain new series as task/status combinations
# appear, so ranges are computed with increase() (per-series and reset-aware) and aggregated
# only afterwards. Counts read slightly low for a series' first run, which is accepted: the
# birth-aware alternatives measured non-monotonic under scrape gaps.

def delta(metric_sel, by='', rng='$__range'):
    """Count of discrete events in the window; rounded because increase() extrapolates."""
    return 'round(sum%s(increase(%s[%s])))' % (by, metric_sel, rng)

def total(metric_sel, by='', rng='$__range'):
    """Accumulated seconds in the window — a duration, so not rounded."""
    return 'sum%s(increase(%s[%s]))' % (by, metric_sel, rng)

def mean(sum_sel, count_sel, by='', rng='$__range'):
    """Mean duration from a _sum/_count pair. `> 0` guards against divide-by-zero (+Inf)."""
    return '%s / (%s > 0)' % (total(sum_sel, by, rng), total(count_sel, by, rng))

def share(num_sel, den_sel, by='', rng='$__range'):
    """Ratio of two event counts (success rate, conversion rate), with the same zero guard."""
    return '%s / (%s > 0)' % (total(num_sel, by, rng), total(den_sel, by, rng))

def pctl(q, bucket_sel, count_sel, label, rng='$__range'):
    """Duration percentile from the histogram buckets. Preferred over the mean, which a few
    hung failures drag far above a healthy run. `and on()` drops idle entries that would
    otherwise render as NaN."""
    return ('histogram_quantile(%s, sum by (%s, le)(increase(%s[%s])))'
            ' and on(%s) (sum by (%s)(increase(%s[%s])) > 0)'
            % (q, label, bucket_sel, rng, label, label, count_sel, rng))

def distinct(metric_sel, label, rng='$__range'):
    """Distinct values of `label` that recorded an event in the window."""
    return 'count(sum by (%s)(increase(%s[%s])) > 0)' % (label, metric_sel, rng)

# ---- panel builders ------------------------------------------------------
def stat(pid, title, x, w, expr, unit='none', decimals=0, no_value='0',
         thresholds=None, fixed_color=None, y=0, h=4, mappings=None, description=None):
    fc = {"unit": unit, "decimals": decimals, "noValue": no_value}
    if thresholds:
        fc["thresholds"] = {"mode": "absolute", "steps": thresholds}
    if fixed_color:
        fc["color"] = {"mode": "fixed", "fixedColor": fixed_color}
    if mappings:
        fc["mappings"] = mappings
    p = {"id": pid, "type": "stat", "title": title,
         "gridPos": {"h": h, "w": w, "x": x, "y": y},
         "datasource": DS,
         "targets": [{"refId": "A", "expr": expr, "instant": True}],
         "fieldConfig": {"defaults": fc, "overrides": []},
         "options": {"graphMode": "none", "colorMode": "value",
                     "reduceOptions": {"calcs": ["lastNotNull"]}}}
    if description: p["description"] = description
    return p

def timeseries(pid, title, x, y, w, h, targets, unit='none', decimals=None,
               draw='line', stacked=False, fill=None, overrides=None,
               description=None, point_size=None, min_val=0):
    custom = {"drawStyle": draw, "lineWidth": 2 if draw == 'line' else 0,
              "fillOpacity": fill if fill is not None else (85 if draw == 'bars' else 0),
              "spanNulls": False, "pointSize": point_size or 5}
    if stacked:
        custom["stacking"] = {"mode": "normal", "group": "A"}
    defaults = {"unit": unit, "min": min_val, "custom": custom}
    if decimals is not None:
        defaults["decimals"] = decimals
    p = {"id": pid, "type": "timeseries", "title": title,
         "gridPos": {"h": h, "w": w, "x": x, "y": y},
         "datasource": DS, "targets": targets,
         "fieldConfig": {"defaults": defaults, "overrides": overrides or []},
         "options": {"legend": {"displayMode": "list", "placement": "bottom", "showLegend": True},
                     "tooltip": {"mode": "multi", "sort": "desc"}}}
    if description: p["description"] = description
    return p

def tgt(expr, legend=None, refid='A', interval=None, instant=False, table=False):
    t = {"refId": refid, "expr": expr}
    if legend: t["legendFormat"] = legend
    if interval: t["interval"] = interval
    if instant: t["instant"] = True
    if table: t["format"] = "table"
    return t

def table(pid, title, x, y, w, h, targets, renames, units=None, sort_by=None,
          description=None, transformations=None):
    """renames: {'Value #A': 'Runs', ...}; units: {'Runs': ('s', 1)}"""
    trans = transformations or []
    org = {"id": "organize",
           "options": {"excludeByName": {"Time": True, "Time 1": True, "Time 2": True, "Time 3": True},
                       "renameByName": renames}}
    trans = trans + [org]
    overrides = []
    for col, (unit, dec) in (units or {}).items():
        overrides.append({"matcher": {"id": "byName", "options": col},
                          "properties": [{"id": "unit", "value": unit},
                                         {"id": "decimals", "value": dec}]})
    p = {"id": pid, "type": "table", "title": title,
         "gridPos": {"h": h, "w": w, "x": x, "y": y},
         "datasource": DS, "targets": targets,
         "transformations": trans,
         "fieldConfig": {"defaults": {"unit": "none", "decimals": 0}, "overrides": overrides},
         "options": {}}
    if sort_by:
        p["options"]["sortBy"] = [{"displayName": sort_by, "desc": True}]
    if description: p["description"] = description
    return p


def donut(pid, title, x, y, w, h, targets, unit='none', decimals=0, description=None):
    """Donut for ADDITIVE part-of-whole compositions only (never peaks/averages)."""
    p = {"id": pid, "type": "piechart", "title": title,
         "gridPos": {"h": h, "w": w, "x": x, "y": y},
         "datasource": DS, "targets": targets,
         "fieldConfig": {"defaults": {"unit": unit, "decimals": decimals}, "overrides": []},
         "options": {"pieType": "donut",
                     "reduceOptions": {"calcs": ["lastNotNull"]},
                     "legend": {"displayMode": "table", "placement": "right",
                                "showLegend": True, "values": ["value", "percent"]},
                     "tooltip": {"mode": "single"}}}
    if description: p["description"] = description
    return p

def var_query(name, query, ds=DS):
    return {"name": name, "type": "query", "datasource": ds, "query": query,
            "refresh": 2, "includeAll": True, "multi": True,
            "current": {"text": "All", "value": "$__all"}}

def dashboard(uid, title, panels, variables):
    return {"uid": uid, "title": title, "tags": ["tekton", "krci"],
            "timezone": "browser", "schemaVersion": 39, "editable": True,
            "time": {"from": "now-24h", "to": "now"}, "refresh": "1m",
            "templating": {"list": variables}, "panels": panels}

STATUS_OVERRIDES = [
    {"matcher": {"id": "byName", "options": "success"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "green"}}]},
    {"matcher": {"id": "byName", "options": "failed"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "red"}}]},
    {"matcher": {"id": "byName", "options": "cancelled"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "orange"}}]},
]

# =========================================================================
# D2 — Task Analytics
# =========================================================================
TSEL = 'namespace=~"$namespace", pipeline=~"$pipeline", task=~"$task"'
TC = 'tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_count{%s}' % TSEL
TB = 'tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_bucket{%s}' % TSEL
TS_ = 'tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_sum{%s}' % TSEL
TCF = 'tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_count{%s, status!="success"}' % TSEL

d2 = dashboard('tekton-task-analytics', 'Tekton / Task Analytics', [
    stat(1, 'Task runs (range)', 0, 6, delta(TC), fixed_color='text',
         description='TaskRuns that completed in the selected range.'),
    stat(2, 'Failed task runs (range)', 6, 6, delta(TCF), no_value='0',
         thresholds=[{"color": "text", "value": None}, {"color": "red", "value": 1}],
         description='TaskRuns that did not succeed. Always a subset of Task runs.'),
    stat(3, 'Tasks that ran (range)', 12, 6, distinct(TC, 'task'), fixed_color='text',
         description='Distinct task names that ran in the selected range — not every task the platform knows about.'),
    stat(4, 'Avg task duration (range)', 18, 6, mean(TS_, TC),
         unit='s', decimals=1, no_value='n/a', fixed_color='text'),
    table(5, 'Slowest tasks — typical vs tail (range)', 0, 4, 12, 9,
          [tgt(pctl('0.95', TB, TC, 'task'), refid='A', instant=True, table=True),
           tgt(pctl('0.50', TB, TC, 'task'), refid='B', instant=True, table=True),
           tgt(mean(TS_, TC, ' by (task)'), refid='C', instant=True, table=True)],
          {"Value #A": "p95", "Value #B": "p50 (typical)", "Value #C": "Avg"},
          units={"p95": ("s", 1), "p50 (typical)": ("s", 1), "Avg": ("s", 1)}, sort_by="p95",
          transformations=[{"id": "joinByField", "options": {"byField": "task", "mode": "outer"}}],
          description='p50 is what a healthy run costs, p95 is the tail. A large Avg/p50 gap means the task hangs when it fails rather than being slow.'),
    donut(6, 'Time budget by task (range)', 12, 4, 12, 9,
          [tgt('topk(8, %s)' % total(TS_, ' by (task)'), legend='{{task}}', instant=True)],
          unit='s',
          description='Share of total wall-clock consumed per task across ALL runs (frequency x duration) — where the platform spends its time. Top 8.'),
    timeseries(7, 'Task runs per interval by status', 0, 13, 12, 9,
               [tgt(delta(TC, ' by (status)', '$__interval'), legend='{{status}}', interval='10m')],
               draw='bars', stacked=True, overrides=STATUS_OVERRIDES, decimals=0,
               description='Completed TaskRuns per 10m interval by final status.'),
    timeseries(8, 'Task duration avg per interval', 12, 13, 12, 9,
               [tgt(mean(TS_, TC, ' by (task)', '$__interval'), legend='{{task}}', interval='10m')],
               unit='s', draw='points', point_size=8,
               description='Average duration of task runs completed in each 10m interval. Narrow with the task/pipeline filters.'),
    table(9, 'Task failures by class (range)', 0, 22, 12, 8,
          [tgt(delta(TCF, ' by (task, reason)'), instant=True, table=True)],
          {"Value": "Failures", "reason": "Failure class"},
          units={"Failures": ("none", 0)}, sort_by="Failures",
          description='Failed tasks grouped by the Tekton failure class (Failed, TaskRunTimeout, Cancelled). Use the TaskRun logs for the root cause.'),
    table(10, 'Per-task summary (range)', 12, 22, 12, 8,
          [tgt(delta(TC, ' by (task)'), refid='A', instant=True, table=True),
           tgt(delta(TCF, ' by (task)'), refid='B', instant=True, table=True),
           tgt(pctl('0.50', TB, TC, 'task'), refid='C', instant=True, table=True),
           tgt(pctl('0.95', TB, TC, 'task'), refid='D', instant=True, table=True),
           tgt(mean(TS_, TC, ' by (task)'), refid='E', instant=True, table=True)],
          {"Value #A": "Runs", "Value #B": "Failures", "Value #C": "p50 (typical)",
           "Value #D": "p95", "Value #E": "Avg duration"},
          units={"p50 (typical)": ("s", 1), "p95": ("s", 1), "Avg duration": ("s", 1)}, sort_by="Runs",
          transformations=[{"id": "joinByField", "options": {"byField": "task", "mode": "outer"}}]),
], [
    var_query('namespace', 'label_values(tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_count, namespace)'),
    var_query('pipeline', 'label_values(tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_count{namespace=~"$namespace"}, pipeline)'),
    var_query('task', 'label_values(tekton_pipelines_controller_pipelinerun_taskrun_duration_seconds_count{namespace=~"$namespace", pipeline=~"$pipeline"}, task)'),
])

# =========================================================================
# D3 — Queue & Scheduling
# =========================================================================
PEND = 'kube_pod_status_phase{namespace=~"$namespace", phase="Pending", pod=~".*-pod.*"}'
d3 = dashboard('tekton-queue-scheduling', 'Tekton / Queue & Scheduling', [
    stat(1, 'Pending task pods now', 0, 6, 'sum(%s) or vector(0)' % PEND,
         thresholds=[{"color": "green", "value": None}, {"color": "orange", "value": 1}, {"color": "red", "value": 5}],
         description='Task pods waiting to be scheduled (pod name heuristic: *-pod*).'),
    stat(2, 'Throttled by ResourceQuota', 6, 6,
         'sum(tekton_pipelines_controller_running_taskruns_throttled_by_quota) or vector(0)',
         thresholds=[{"color": "green", "value": None}, {"color": "red", "value": 1}]),
    stat(3, 'Throttled by node capacity', 12, 6,
         'sum(tekton_pipelines_controller_running_taskruns_throttled_by_node) or vector(0)',
         thresholds=[{"color": "green", "value": None}, {"color": "red", "value": 1}]),
    stat(4, 'Waiting on resolution', 18, 6,
         '(sum(tekton_pipelines_controller_running_pipelineruns_waiting_on_pipeline_resolution) or vector(0)) + (sum(tekton_pipelines_controller_running_pipelineruns_waiting_on_task_resolution) or vector(0))',
         thresholds=[{"color": "green", "value": None}, {"color": "orange", "value": 1}],
         description='PipelineRuns blocked resolving pipeline/task refs (resolver latency).'),
    timeseries(5, 'Pending task pods', 0, 4, 12, 8,
               [tgt('sum(%s)' % PEND, legend='pending task pods')],
               decimals=0, fill=20, description='Queue depth proxy: task pods in Pending phase (scheduling + image pull wait).'),
    timeseries(6, 'Running PipelineRuns / TaskRuns', 12, 4, 12, 8,
               [tgt('sum(tekton_pipelines_controller_running_pipelineruns)', legend='pipelineruns'),
                tgt('sum(tekton_pipelines_controller_running_taskruns)', legend='taskruns', refid='B')],
               decimals=0, description='Live concurrency on the cluster.'),
    timeseries(7, 'TaskRuns throttled', 0, 12, 12, 8,
               [tgt('sum(tekton_pipelines_controller_running_taskruns_throttled_by_quota)', legend='by ResourceQuota'),
                tgt('sum(tekton_pipelines_controller_running_taskruns_throttled_by_node)', legend='by node capacity', refid='B')],
               decimals=0, fill=20,
               description='Runs whose pods kubernetes refuses to start. Sustained non-zero = capacity problem.'),
    timeseries(8, 'PipelineRuns waiting on resolution', 12, 12, 12, 8,
               [tgt('sum(tekton_pipelines_controller_running_pipelineruns_waiting_on_pipeline_resolution)', legend='pipeline ref'),
                tgt('sum(tekton_pipelines_controller_running_pipelineruns_waiting_on_task_resolution)', legend='task refs', refid='B')],
               decimals=0),
    table(9, 'Pod scheduling latency — recent pods (top 15)', 0, 20, 14, 8,
          [tgt('topk(15, tekton_pipelines_controller_taskruns_pod_latency_milliseconds{namespace=~"$namespace"})', instant=True, table=True)],
          {"Value": "Latency", "namespace": "namespace", "task": "task", "pod": "pod"},
          units={"Latency": ("ms", 0)}, sort_by="Latency",
          description='Time from TaskRun start to pod scheduled. Gauge per pod: reflects recent pods only; resets with the controller.'),
    timeseries(10, 'Controller workqueue latency p95', 14, 20, 10, 8,
               [tgt('histogram_quantile(0.95, sum by (le) (rate(tekton_pipelines_controller_workqueue_queue_latency_seconds_bucket[$__rate_interval])))', legend='p95 queue wait')],
               unit='s', description='How long reconcile work waits in the controller queue — controller saturation signal.'),
], [
    var_query('namespace', 'label_values(tekton_pipelines_controller_pipelinerun_duration_seconds_count, namespace)'),
])

# =========================================================================
# D4 — Resource Consumption
# =========================================================================
CSEL = 'namespace=~"$namespace", pod=~".*-pod.*", container!="", container!="POD"'
CPU = 'container_cpu_usage_seconds_total{%s}' % CSEL
MEM = 'container_memory_working_set_bytes{%s}' % CSEL
d4 = dashboard('tekton-resource-consumption', 'Tekton / Resource Consumption', [
    stat(1, 'Task pods CPU now', 0, 6, 'sum(rate(%s[5m])) or vector(0)' % CPU,
         unit='none', decimals=2, fixed_color='text', description='Sum of CPU cores used by task pods right now.'),
    stat(2, 'Task pods memory now', 6, 6, 'sum(%s) or vector(0)' % MEM,
         unit='bytes', decimals=1, fixed_color='text'),
    stat(3, 'CPU time consumed (range)', 12, 6, 'sum(increase(%s[$__range])) or vector(0)' % CPU,
         unit='s', decimals=0, fixed_color='text', description='Total CPU-seconds burned by task pods in the range.'),
    stat(4, 'Peak task-pod memory (range)', 18, 6, 'max(max_over_time(%s[$__range])) or vector(0)' % MEM,
         unit='bytes', decimals=1, fixed_color='text'),
    timeseries(5, 'CPU by task pod', 0, 4, 12, 9,
               [tgt('sum by (pod) (rate(%s[5m]))' % CPU, legend='{{pod}}')],
               decimals=2, description='CPU cores per task pod (5m rate). Pod names encode pipelinerun + task.'),
    timeseries(6, 'Memory (working set) by task pod', 12, 4, 12, 9,
               [tgt('sum by (pod) (%s)' % MEM, legend='{{pod}}')],
               unit='bytes', description='Working-set memory per task pod.'),
    table(7, 'Top 10 peak memory by image (range)', 0, 13, 12, 9,
          [tgt('topk(10, max by (image) (max_over_time(%s[$__range])))' % MEM, instant=True, table=True)],
          {"Value": "Peak memory"}, units={"Peak memory": ("bytes", 1)}, sort_by="Peak memory",
          description='Which task images are the memory hogs — informs task resource requests/limits.'),
    donut(8, 'CPU time share by image (range)', 12, 13, 12, 9,
          [tgt('topk(8, sum by (image) (increase(%s[$__range])))' % CPU, legend='{{image}}', instant=True)],
          unit='s',
          description='Share of total CPU-seconds per task image over the range (additive). Top 8.'),
], [
    var_query('namespace', 'label_values(kube_pod_status_phase, namespace)'),
])

# =========================================================================
# D5 — EventListener Traffic
# =========================================================================
E = 'eventlistener_event_received_total{eventlistener=~"$eventlistener"}'
EF = 'eventlistener_event_received_total{eventlistener=~"$eventlistener", status!="succeeded"}'
T = 'eventlistener_triggered_resources_total{eventlistener=~"$eventlistener"}'
HS = 'eventlistener_http_duration_seconds_sum{eventlistener=~"$eventlistener"}'
HC = 'eventlistener_http_duration_seconds_count{eventlistener=~"$eventlistener"}'
d5 = dashboard('tekton-eventlistener-traffic', 'Tekton / EventListener Traffic', [
    stat(1, 'Events received (range)', 0, 5, delta(E), fixed_color='text'),
    stat(2, 'Failed events (range)', 5, 5, delta(EF),
         thresholds=[{"color": "text", "value": None}, {"color": "red", "value": 1}],
         description='Webhook payloads that did not process successfully (bad payload, interceptor reject, sink error).'),
    stat(3, 'PipelineRuns triggered (range)', 10, 5, delta(T), fixed_color='text'),
    stat(4, 'Events → runs conversion', 15, 5, share(T, E),
         unit='percentunit', decimals=0, no_value='n/a', fixed_color='text',
         description='Triggered resources / received events. Low = most webhooks filtered out by interceptors (expected for push/comment noise).'),
    stat(5, 'Listeners up', 20, 4, 'sum(up{job=~"el-.*"}) or vector(0)',
         thresholds=[{"color": "red", "value": None}, {"color": "green", "value": 1}]),
    timeseries(6, 'Events received per interval', 0, 4, 12, 9,
               [tgt(delta(E, ' by (eventlistener, status)', '$__interval'),
                    legend='{{eventlistener}} / {{status}}', interval='10m')],
               draw='bars', stacked=True, decimals=0,
               description='Webhook payloads per 10m interval, per listener and processing status.'),
    timeseries(7, 'Resources triggered per interval', 12, 4, 12, 9,
               [tgt(delta(T, ' by (eventlistener, kind)', '$__interval'),
                    legend='{{eventlistener}} / {{kind}}', interval='10m')],
               draw='bars', stacked=True, decimals=0,
               description='Resources (PipelineRuns) created per 10m interval, per listener.'),
    timeseries(8, 'Webhook processing latency (avg per interval)', 0, 13, 12, 8,
               [tgt(mean(HS, HC, ' by (eventlistener)', '$__interval'),
                    legend='{{eventlistener}}', interval='10m')],
               unit='s', draw='points', point_size=8,
               description='EventListener HTTP handler time. This is payload processing only — the PipelineRun creation is async.'),
    timeseries(9, 'Listener availability', 12, 13, 12, 8,
               [tgt('up{job=~"el-.*"}', legend='{{job}}')],
               decimals=0, draw='line', fill=10,
               description='Scrape success per listener service (1 = up).'),
], [
    var_query('eventlistener', 'label_values(eventlistener_event_received_total, eventlistener)'),
])

# =========================================================================
# D6 — Platform Health
# =========================================================================
SHORT_REC = 'label_replace(%s, "reconciler", "$1", "reconciler", ".*\\\\.([^.]+)\\\\.Reconciler")'
RL = 'sum by (reconciler, le) (rate(tekton_pipelines_controller_reconcile_latency_bucket[$__rate_interval]))'
d6 = dashboard('tekton-platform-health', 'Tekton / Platform Health', [
    table(1, 'Scrape targets', 0, 0, 10, 8,
          [tgt('up{job=~"tekton-.*|el-.*|.*results.*"}', instant=True, table=True)],
          {"Value": "Up", "job": "job", "namespace": "namespace"},
          sort_by="Up",
          description='Prometheus scrape state per component. Any DOWN means blind spots in every other dashboard.'),
    timeseries(2, 'Reconcile latency p95 by reconciler', 10, 0, 14, 8,
               [tgt('histogram_quantile(0.95, %s)' % (SHORT_REC % RL), legend='{{reconciler}}')],
               unit='ms', description='Controller reconcile duration p95. Rising = controller falling behind.'),
    timeseries(3, 'Reconcile outcomes per interval', 0, 8, 12, 8,
               [tgt(SHORT_REC % 'sum by (reconciler, success) (rate(tekton_pipelines_controller_reconcile_count[$__rate_interval]))',
                    legend='{{reconciler}} success={{success}}')],
               unit='ops', decimals=2,
               description='Reconciles/sec. success=false includes benign requeues (running PipelineRuns re-queue constantly) — watch the trend, not the absolute value.'),
    timeseries(4, 'Controller workqueue depth', 12, 8, 12, 8,
               [tgt('sum by (name) (label_replace(tekton_pipelines_controller_workqueue_depth, "name", "$1", "name", ".*\\\\.([^.]+\\\\.Reconciler.*)"))', legend='{{name}}')],
               decimals=0, description='Items waiting for reconcile. Sustained growth = controller saturation.'),
    timeseries(5, 'Results API gRPC errors', 0, 16, 12, 8,
               [tgt('sum by (grpc_code, grpc_method) (rate(grpc_server_handled_total{grpc_code!~"OK|NotFound"}[$__rate_interval])) > 0', legend='{{grpc_method}} {{grpc_code}}')],
               unit='ops', decimals=3,
               description='Non-OK responses from the Results API, excluding benign NotFound (Portal polls runs before archival). Empty panel = healthy.'),
    timeseries(6, 'Results watcher: PipelineRuns pruned per interval', 12, 16, 12, 8,
               [tgt(delta('watcher_pipelinerun_delete_count_total', ' by (status)', '$__interval'),
                    legend='{{status}}', interval='10m')],
               draw='bars', stacked=True, decimals=0, overrides=STATUS_OVERRIDES,
               description='Completed runs archived to Results and deleted from the cluster. status=failed here means the DELETE failed — runs pile up.'),
], [])


# ---- post-process: strip leaked scrape labels, colorize Up column --------
LEAK = {"__name__": True, "endpoint": True, "instance": True, "container": True,
        "service": True, "job": True, "reason": True}
for panel in d3['panels']:
    if panel['id'] == 9:
        panel['transformations'][-1]['options']['excludeByName'].update(LEAK)
for panel in d6['panels']:
    if panel['id'] == 1:
        panel['transformations'][-1]['options']['excludeByName'].update(
            {"__name__": True, "endpoint": True, "instance": True, "container": True,
             "service": True, "pod": True, "eventlistener": True})
        panel['fieldConfig']['overrides'].append(
            {"matcher": {"id": "byName", "options": "Up"},
             "properties": [
                 {"id": "mappings", "value": [{"type": "value", "options": {
                     "1": {"text": "UP", "color": "green", "index": 0},
                     "0": {"text": "DOWN", "color": "red", "index": 1}}}]},
                 {"id": "custom.cellOptions", "value": {"type": "color-background"}}]})

# =========================================================================
# D1 — Pipeline Overview
# =========================================================================
# Previously hand-authored in Grafana and only patched here (panel 7). It carried the same
# broken offset-subtraction in 8 of its 9 panels, so it is now generated in full like the rest.
PSEL = 'namespace=~"$namespace", pipeline=~"$pipeline"'
PC = 'tekton_pipelines_controller_pipelinerun_duration_seconds_count{%s}' % PSEL
PB = 'tekton_pipelines_controller_pipelinerun_duration_seconds_bucket{%s}' % PSEL
PS_ = 'tekton_pipelines_controller_pipelinerun_duration_seconds_sum{%s}' % PSEL
PCOK = 'tekton_pipelines_controller_pipelinerun_duration_seconds_count{%s, status="success"}' % PSEL
PCF = 'tekton_pipelines_controller_pipelinerun_duration_seconds_count{%s, status=~"failed|error"}' % PSEL
PCTO = 'tekton_pipelines_controller_pipelinerun_duration_seconds_count{%s, reason=~".*Timeout.*"}' % PSEL
PCNOK = 'tekton_pipelines_controller_pipelinerun_duration_seconds_count{%s, status!="success"}' % PSEL

REASON_OVERRIDES = [
    {"matcher": {"id": "byName", "options": "Failed"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "red"}}]},
    {"matcher": {"id": "byRegexp", "options": ".*Timeout.*"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "orange"}}]},
    {"matcher": {"id": "byRegexp", "options": ".*[Cc]ancel.*"},
     "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "yellow"}}]}]

d1 = dashboard('tekton-pipeline-overview', 'Tekton / Pipeline Overview', [
    stat(1, 'Runs (range)', 0, 5, delta(PC), fixed_color='text'),
    stat(2, 'Success rate', 5, 5, share(PCOK, PC), unit='percentunit', decimals=1,
         no_value='n/a',
         thresholds=[{"color": "red", "value": None}, {"color": "orange", "value": 0.8},
                     {"color": "green", "value": 0.95}]),
    stat(3, 'Failed runs (range)', 10, 5, delta(PCF),
         thresholds=[{"color": "text", "value": None}, {"color": "red", "value": 1}]),
    stat(4, 'Timeouts (range)', 15, 5, delta(PCTO),
         thresholds=[{"color": "text", "value": None}, {"color": "red", "value": 1}],
         description='PipelineRuns that hit their timeout rather than failing on their own.'),
    stat(5, 'Running now', 20, 4, 'sum(tekton_pipelines_controller_running_pipelineruns{pipeline=~"$pipeline"})',
         fixed_color='blue'),
    timeseries(6, 'Pipeline runs by result', 0, 4, 14, 9,
               [tgt(delta(PC, ' by (status)', '$__interval'), legend='{{status}}', interval='10m')],
               draw='bars', stacked=True, overrides=STATUS_OVERRIDES, decimals=0,
               description='Completed PipelineRuns per 10m interval, split by final status.'),
    # Names the empty-reason series so a missing `reason` label reads as "unlabelled" rather
    # than Grafana's anonymous "Value" wedge, which looks like a real result.
    donut(7, 'Failure reasons (range)', 14, 4, 10, 9,
          [tgt('label_replace(%s, "reason", "unlabelled", "reason", "^$")'
               % delta(PCNOK, ' by (reason)'), legend='{{reason}}', instant=True)],
          description='Non-success PipelineRuns by failure class — separates broken builds (Failed) from an overloaded cluster (PipelineRunTimeout) and deliberate stops (Cancelled).'),
    timeseries(8, 'Pipeline run duration (avg per interval)', 0, 13, 14, 9,
               [tgt(mean(PS_, PC, ' by (pipeline)', '$__interval'), legend='{{pipeline}}', interval='10m')],
               unit='s', draw='points', point_size=9,
               description='Mean duration of runs completed in each 10m interval, per pipeline. Isolated spikes are usually failures hanging until timeout, not a slowdown.'),
    table(9, 'Per-pipeline summary (range)', 14, 13, 10, 9,
          [tgt(delta(PC, ' by (pipeline)'), refid='A', instant=True, table=True),
           tgt(share(PCOK, PC, ' by (pipeline)'), refid='B', instant=True, table=True),
           tgt(pctl('0.50', PB, PC, 'pipeline'), refid='C', instant=True, table=True),
           tgt(pctl('0.95', PB, PC, 'pipeline'), refid='D', instant=True, table=True),
           tgt(mean(PS_, PC, ' by (pipeline)'), refid='E', instant=True, table=True)],
          {"Value #A": "Runs", "Value #B": "Success rate", "Value #C": "p50 (typical)",
           "Value #D": "p95", "Value #E": "Avg duration"},
          units={"Success rate": ("percentunit", 1), "p50 (typical)": ("s", 1),
                 "p95": ("s", 1), "Avg duration": ("s", 1)}, sort_by="Runs",
          transformations=[{"id": "joinByField", "options": {"byField": "pipeline", "mode": "outer"}}]),
], [
    var_query('namespace', 'label_values(tekton_pipelines_controller_pipelinerun_duration_seconds_count, namespace)'),
    var_query('pipeline', 'label_values(tekton_pipelines_controller_pipelinerun_duration_seconds_count{namespace=~"$namespace"}, pipeline)'),
])
d1['panels'][6]['fieldConfig']['overrides'] = REASON_OVERRIDES

# ---- emit ----------------------------------------------------------------
os.makedirs(OUT, exist_ok=True)
for name, d in [('tekton-pipeline-overview', d1), ('tekton-task-analytics', d2),
                ('tekton-queue-scheduling', d3), ('tekton-resource-consumption', d4),
                ('tekton-eventlistener-traffic', d5), ('tekton-platform-health', d6)]:
    with open(os.path.join(OUT, name + '.json'), 'w') as f:
        json.dump(d, f, indent=2)
    print('wrote', name)
