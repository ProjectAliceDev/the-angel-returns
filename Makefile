.PHONY: release

default: dev

dev:
	bash scripts/make_dev.sh
    
release:
	bash scripts/make_release.sh
