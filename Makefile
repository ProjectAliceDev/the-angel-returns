.PHONY: release

default: dev

dev:
    wget https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
    tar xf renpy-6.99.12.4-sdk.tar.bz2
    rm renpy-6.99.12.4-sdk.tar.bz2
    mv renpy-6.99.12.4-sdk renpy
    rm -rf renpy-6.99.12.4-sdk
    bash ./setup.sh
    bash -c "echo "{\"version\":\"local\"}" >> version"
    cd renpy 
    ./renpy.sh "../" lint && ./renpy.sh launcher distribute "../"
    
release:
    wget https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
    tar xf renpy-6.99.12.4-sdk.tar.bz2
    rm renpy-6.99.12.4-sdk.tar.bz2
    mv renpy-6.99.12.4-sdk renpy
    rm -rf renpy-6.99.12.4-sdk
    bash ./setup.sh
    bash print_version.sh
    cd renpy 
    ./renpy.sh "../" lint && ./renpy.sh launcher distribute "../"