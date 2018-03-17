#!/bin/bash

# copy pics folder
rm -rf pics_copy
cp -r pics pics_copy

# deploy to google app engine
gcloud auth activate-service-account travis-deploy@app-xkcd-cn.iam.gserviceaccount.com --key-file=key.json
gcloud config set project app-xkcd-cn
gcloud app deploy --version 20180311t034401 --quiet
