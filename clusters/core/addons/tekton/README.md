# Tekton Results — PostgreSQL Performance Indexes

Tekton Results (v0.17.2) stores PipelineRun/TaskRun data in PostgreSQL via GORM auto-migration.
The default schema has no indexes beyond primary keys, causing sequential scans on high-traffic query paths.

## Indexes

### 1. `idx_records_parent_type_created`

B-tree on `records(parent, type, created_time DESC)`. Covers list queries filtered by parent/type and sorted by time.

```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_records_parent_type_created
  ON records (parent, type, created_time DESC);
```

### 2. `results_annotations`

GIN on `results.annotations`. Covers JSONB containment queries (`@>`) for codebase/name filtering.

```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS results_annotations
  ON results USING GIN (annotations jsonb_path_ops);
```

### 3. `record_summary_annotations` (optional)

GIN on `results.recordsummary_annotations`. Future-proofing for DORA metrics queries. Only create if your deployment uses `recordsummary_annotations` filtering.

```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS record_summary_annotations
  ON results USING GIN (recordsummary_annotations jsonb_path_ops);
```

## Applying via kubectl (PGO Operator)

PostgreSQL is deployed via [Crunchy PGO](https://access.crunchydata.com/documentation/postgres-operator/v5/) `PostgresCluster` CR named `results` in `tekton-pipelines` namespace.

### Find the primary pod

```bash
PG_POD=$(kubectl get pods -n tekton-pipelines \
  -l postgres-operator.crunchydata.com/cluster=results,postgres-operator.crunchydata.com/role=master \
  -o jsonpath='{.items[0].metadata.name}')
```

### Apply indexes

`CREATE INDEX CONCURRENTLY` cannot run inside a transaction block, so run each statement separately:

```bash
kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c \
  "CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_records_parent_type_created ON records (parent, type, created_time DESC);"

kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c \
  "CREATE INDEX CONCURRENTLY IF NOT EXISTS results_annotations ON results USING GIN (annotations jsonb_path_ops);"

kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c \
  "CREATE INDEX CONCURRENTLY IF NOT EXISTS record_summary_annotations ON results USING GIN (recordsummary_annotations jsonb_path_ops);"
```

### Verify indexes exist

```bash
kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c "\di+"
```

### Verify index is used

```bash
kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c "
    EXPLAIN ANALYZE
    SELECT * FROM records
    WHERE parent LIKE 'tekton-pipelines/results/%'
      AND type = 'tekton.dev/v1.PipelineRun'
    ORDER BY created_time DESC
    LIMIT 10;
  "
```

Expect `Index Scan` or `Bitmap Index Scan` using `idx_records_parent_type_created`, not `Seq Scan`.

## Rollback

```bash
kubectl exec -it -n tekton-pipelines "$PG_POD" -c database -- \
  psql -U postgres -d results -c "
    DROP INDEX IF EXISTS idx_records_parent_type_created;
    DROP INDEX IF EXISTS results_annotations;
    DROP INDEX IF EXISTS record_summary_annotations;
  "
```
