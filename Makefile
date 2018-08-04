.PHONY: release

default: dev

dev:

	bash scripts/make_release.sh
    
release:

	bash scripts/make_release.sh

test:
	bash scripts/setup.sh