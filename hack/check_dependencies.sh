#!/bin/bash

set -e

update_helm_repos() {
    helm repo update > /dev/null 2>/dev/null || true
}

process_chart() {
    find clusters -type f -name 'Chart.yaml' | while read -r chart_yaml; do
        yq eval '.dependencies[] | .name + " " + .version + " " + .repository' "$chart_yaml" | while read -r name version repo; do
            if [[ "$repo" != oci://* ]]; then
                helm repo add "$name" "$repo" --force-update > /dev/null
                latest_version=$(helm search repo "$name/$name" -o yaml | yq e '.[0].version' - 2>/dev/null)
            else
                latest_version=$(helm show chart "$repo/$name" 2>/dev/null | yq e '.version' - 2>/dev/null)
            fi

            printf "| %-24s | %-15s | %-15s | %-54s |\n" "$name" "$version" "$latest_version" "$chart_yaml"
        done
    done
}

echo "+--------------------------+-----------------+-----------------+--------------------------------------------------------+"
echo "| Dependency Name          | Current Version | Latest Version  | Path                                                   |"
echo "+--------------------------+-----------------+-----------------+--------------------------------------------------------+"

update_helm_repos
process_chart

echo "+--------------------------+-----------------+-----------------+--------------------------------------------------------+"
