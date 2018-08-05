#!/bin/sh

if ! [ -z "$TRAVIS_TAG" ]; then
    touch ../mod/version;
    echo "{\"version\":\"$TRAVIS_TAG\"}" >> ../mod/version;
    echo "{\"version\":\"$TRAVIS_TAG\"}" >> version;
    exit 0;
else
    touch ../mod/version;
    echo "{\"version\":\"$(printf 'local')\"}" >> ../mod/version;
    echo "{\"version\":\"$(printf 'local')\"}" >> version;
    exit 0;
fi