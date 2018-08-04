.PHONY: release

default: dev

dev:
    bash build/make_dev.sh
release:
    bash build/make_release.sh

ci:
  if [[-z "$TRAVIS_TAG"]]; then
     release 
  else 
     dev
  fi