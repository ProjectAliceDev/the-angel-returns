#!/bin/bash

if [[ -f "renpy-6.99.12.4-sdk.tar.bz2.tar.bz2" ]]; then
    tar xf renpy-6.99.12.4-sdk.tar.bz2
    rm renpy-6.99.12.4-sdk.tar.bz2
    mv renpy-6.99.12.4-sdk renpy
    rm -rf renpy-6.99.12.4-sdk
    bash scripts/setup.sh
    echo "{\"version\":\"$(printf "local")\"}" >> version
    cd renpy 
    ./renpy.sh "../" lint && ./renpy.sh launcher distribute "../"
else 
    wget https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
    tar xf renpy-6.99.12.4-sdk.tar.bz2
    rm renpy-6.99.12.4-sdk.tar.bz2
    mv renpy-6.99.12.4-sdk renpy
    rm -rf renpy-6.99.12.4-sdk
    bash scripts/setup.sh
    echo "{\"version\":\"$(printf "local")\"}" >> version
    cd renpy
    ./renpy.sh "../" lint && ./renpy.sh launcher distribute "../"
fi
