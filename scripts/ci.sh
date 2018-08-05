#!/bin/bash

if ! [ -z "$TRAVIS_TAG" ]; then 
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Release Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make release;
else
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Developer Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make dev;
fi
