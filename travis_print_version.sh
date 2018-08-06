#!/bin/sh

if ! [ -z "$TRAVIS_TAG" ]; then
    echo "{\"version\":\"$TRAVIS_TAG\"}" | tee mod/version;
else
    touch ../mod/version;
    echo "{\"version\":\"$(printf 'local')\"}" | tee mod/version;
fi