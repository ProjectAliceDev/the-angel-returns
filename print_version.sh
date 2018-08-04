#!/bin/bash

if [[ -z "$CI" ]] && [[ -z "$TRAVIS_TAG" ]]; then
  echo "{\"version\":\"$TRAVIS_TAG\"}" >> version;
  exit 0;
elif [[ ! -z "$TRAVIS_TAG" ]]; then
  echo "No Git tag detected. Exiting.";
  exit 0;
else
  echo "Not in CI! Version is gonna be printed out using Git branch.";
  echo "{\"version\":\"$(git rev-parse --abbrev-ref HEAD)\"}" >> version;  
  exit 0;
fi