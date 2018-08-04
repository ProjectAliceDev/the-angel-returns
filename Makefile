.PHONY: release

default: dev

dev:
    bash scripts/make_release.sh/make_dev.sh
release:
    bash scripts/make_release.sh

ci:
  if [[-z "$TRAVIS_TAG"]]; then
     release 
  else 
     dev
  fi