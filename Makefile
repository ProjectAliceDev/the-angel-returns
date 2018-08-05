.PHONY: release

default: dev

dev:
	bash scripts/make_dev.sh
    
release:
	bash scripts/make_release.sh

travis_dev:
	cd the-angel-returns
	bash scripts/make_dev.sh

travis_release:
	cd the-angel-returns
	bash scripts/make_release.sh