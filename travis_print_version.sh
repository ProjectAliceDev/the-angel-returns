#!/bin/sh

if ! [ -z "$TRAVIS_TAG" ]; then
    echo "{\"version\":\"$TRAVIS_TAG\"}" >> ../mod/version;
    exit 0;
else
    echo "{\"version\":\"$(printf 'local')\"}" >> ../mod/version;  
    exit 0;
fi