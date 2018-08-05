#!/bin/bash

if ! [ -z "$TRAVIS_TAG" ]; then 
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Release Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make release -f "$(pwd)/the-angel-returns/Makefile";
else
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Developer Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make release -f "$(pwd)/the-angel-returns/Makefile";
fi
