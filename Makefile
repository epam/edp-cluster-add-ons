CURRENT_DIR=$(shell pwd)
HELMDOCS = ${CURRENT_DIR}/bin/helm-docs
GITCHGLOG = ${CURRENT_DIR}/bin/git-chglog

# ARGS="--workers 5"

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# use https://github.com/git-chglog/git-chglog/
.PHONY: changelog
changelog: git-chglog	## generate changelog
ifneq (${NEXT_RELEASE_TAG},)
	$(GITCHGLOG) --next-tag v${NEXT_RELEASE_TAG} -o CHANGELOG.md v0.1.0
else
	$(GITCHGLOG) -o CHANGELOG.md v0.1.0..
endif

.PHONY: validate-docs
validate-docs: helm-docs  ## Validate helm docs
	@git diff -s --exit-code */README.md || (echo "Run 'make helm-docs' to address the issue." && git diff && exit 1)

.PHONY: helm-docs
helm-docs: helmdocs	## generate helm docs
	$(HELMDOCS)

.PHONY: helmdocs
helmdocs: ## Download helm-docs locally if necessary.
	$(call go-get-tool,$(HELMDOCS),github.com/norwoodj/helm-docs/cmd/helm-docs,v1.10.0)

.PHONY: git-chglog
git-chglog: ## Download git-chglog locally if necessary.
	$(call go-get-tool,$(GITCHGLOG),github.com/git-chglog/git-chglog/cmd/git-chglog,v0.15.4)

PROJECT_DIR := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
define go-get-tool
@[ -f $(1) ] || { \
set -e ;\
TMP_DIR=$$(mktemp -d) ;\
cd $$TMP_DIR ;\
go mod init tmp ;\
echo "Downloading $(2)" ;\
go get -d $(2)@$(3) ;\
GOBIN=$(PROJECT_DIR)/bin go install $(2) ;\
rm -rf $$TMP_DIR ;\
}
endef

.PHONY: update-readme
update-readme: .venv
	.venv/bin/python ./hack/update_readme.py

.PHONY: check-dependencies
check-dependencies: .venv  ## Check and display Helm dependencies that need updating
	.venv/bin/python ./hack/check_dependencies.py $(ARGS)

.venv:
	virtualenv -p python3 .venv; \
	.venv/bin/pip install -r ./hack/requirements.txt

.PHONY: ci-lint-chart
ci-lint-chart: ## Test charts using chart-testing (lint only), ct will detect changed charts
	@if ! command -v ct > /dev/null; then \
		echo "chart-testing (ct) is not installed. Please install it following instructions at https://github.com/helm/chart-testing#installation"; \
		exit 1; \
	fi
	ct lint --config ct.yaml --lint-conf lint-conf.yaml

.PHONY: lint-all-charts
lint-all-charts: ## Run advanced linting rules against all charts
	@if ! command -v ct > /dev/null; then \
		echo "chart-testing (ct) is not installed. Please install it following instructions at https://github.com/helm/chart-testing#installation"; \
		exit 1; \
	fi
	@echo "Running advanced lint rules from lint-conf.yaml on all charts..."
	ct lint --config ct.yaml --lint-conf lint-conf.yaml --all

.PHONY: lint-chart
lint-chart: ## Lint a specific chart (usage: make lint-chart CHART=chart-name)
	@if ! command -v ct > /dev/null; then \
		echo "chart-testing (ct) is not installed. Please install it following instructions at https://github.com/helm/chart-testing#installation"; \
		exit 1; \
	fi
	@if [ -z "$(CHART)" ]; then \
		echo "Error: CHART variable is not set. Usage: make lint-chart CHART=chart-name"; \
		exit 1; \
	fi
	@echo "Linting chart $(CHART) with rules from lint-conf.yaml..."
	ct lint --config ct.yaml --lint-conf lint-conf.yaml --charts clusters/core/addons/$(CHART)

.PHONY: kind-create
kind-create: ## Create a kind cluster with Kubernetes 1.32 for testing
	@if ! command -v kind > /dev/null; then \
		echo "kind is not installed. Please install it following instructions at https://kind.sigs.k8s.io/docs/user/quick-start/#installation"; \
		exit 1; \
	fi
	@echo "Creating kind cluster with Kubernetes v1.32.0 using kind-config.yaml..."
	@if kind get clusters | grep -q chart-testing; then \
		echo "Using existing chart-testing cluster"; \
	else \
		kind create cluster --config kind-config.yaml --wait 120s; \
	fi
	@echo "Kind cluster 'chart-testing' is ready!"

.PHONY: kind-delete
kind-delete: ## Delete the kind cluster used for testing
	@if ! command -v kind > /dev/null; then \
		echo "kind is not installed. Please install it following instructions at https://kind.sigs.k8s.io/docs/user/quick-start/#installation"; \
		exit 1; \
	fi
	@echo "Deleting kind cluster 'chart-testing'..."
	@if kind get clusters | grep -q chart-testing; then \
		kind delete cluster --name chart-testing; \
		echo "Kind cluster 'chart-testing' has been deleted."; \
	else \
		echo "No 'chart-testing' cluster found."; \
	fi

.PHONY: test-charts-full
test-charts-full: ci-lint-chart kind-create ## Run comprehensive test cycle (lint, install, test)
	@echo "Running full chart testing cycle with all validations..."
	ct install --config ct.yaml
	@echo "Run 'make kind-delete' to remove the test cluster when done."
