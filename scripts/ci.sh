#!/bin/bash

if ! [ -z "$TRAVIS_TAG" ]; then 
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Release Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make travis_dev -f "$(pwd)/the-angel-returns/Makefile";
else
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Developer Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make travis_release -f "$(pwd)/the-angel-returns/Makefile";
fi
