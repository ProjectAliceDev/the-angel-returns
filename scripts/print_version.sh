#!/bin/bash

if [[ -z "$CI" ]] && [[ -z "$TRAVIS_TAG" ]]; then
  echo "{\"version\":\"$TRAVIS_TAG\"}" >> version;
  exit 0;
else
  echo "Not a Release - Version will be printed out using Git branch.";
  echo "{\"version\":\"$(git rev-parse --abbrev-ref HEAD)\"}" >> version;  
  exit 0;
fi
