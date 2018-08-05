#!/bin/bash

if ! [ -z "$TRAVIS_TAG" ]; then 
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Release Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make dev -f "$(pwd)/the-angel-returns/Makefile" -C "$(pwd)/the-angel-returns/";
else
  echo ">>>>>>>>>>>>>>>>>>> Starting Build in Developer Mode. <<<<<<<<<<<<<<<<<<<<<<<"
  make release -f "$(pwd)/the-angel-returns/Makefile" -C "$(pwd)/the-angel-returns/";
fi
