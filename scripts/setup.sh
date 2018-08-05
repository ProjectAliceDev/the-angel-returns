#!/bin/bash

# config for mc
# If you have your own base files, kindly edit this
# However, if you prefer our base files, that's okay too!

mc_endpoint="https://s3-api.us-geo.objectstorage.softlayer.net"
mc_hmac_key="aa1d6f56b97443c185d7282c22adc4a7"
mc_hmac_secret="29fc312082d26720ceeec6e89630f6d2fc382a96c7a72b1c"
mc_alias="ibm"
mc_bucket="filepub"
mc_filename="ddlc_pkg.zip"

# DO NOT EDIT BELOW THIS LINE
# This is intended for automating unzipping and putting the RPAs into the respect folder
if ! [ -z "$(command -v mc)"]; then
   echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Minio S3 Client exists. Skipping install."
   mc config host add $mc_alias $mc_endpoint $mc_hmac_key $mc_hmac_secret && \
   # try if it works
   mc ls $mc_alias;
else 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Installing Minio S3 Client"
wget "https://dl.minio.io/client/mc/release/linux-amd64/mc" && \
chmod +x mc && \
sudo cp -vR mc /usr/bin/mc && \
mc config host add $mc_alias $mc_endpoint $mc_hmac_key $mc_hmac_secret && \
# try if it works
mc ls $mc_alias;
fi

echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Checking for dir if it exists"

if [ -d "./mod" ] && [ -d "./mod/game" ]; then
    # dir exists, just unzip, and make new dir to add file
    echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Directory exists. copying files over."
    mc cp "$mc_alias/$mc_bucket/$mc_filename" ./
    unzip $mc_filename -d  ./game/ 
    exit 0
  else 
    ls
    echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Directory  does not exist. Creating dir and copying files over"
    mc cp "$mc_alias/$mc_bucket/$mc_filename" ./
    mkdir -p "./mod"
    mkdir -p "./mod/game"
    unzip $mc_filename -d  ../game    
    exit 0 
fi
