CURRENT_DIR=$(shell pwd)
HELMDOCS = ${CURRENT_DIR}/bin/helm-docs
GITCHGLOG = ${CURRENT_DIR}/bin/git-chglog

# ARGS="--workers 5"

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
