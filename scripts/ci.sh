#!/bin/bash

if [ -z "$TRAVIS_TAG" ]; then 
  make release;
else
  make dev;
fi
