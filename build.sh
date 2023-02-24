#!/bin/sh

docker build -t progerjkd/glia-jumble .
docker push progerjkd/glia-jumble 

helm uninstall glia-jumble-app
helm install glia-jumble-app -f helm/glia-jumble/values.yaml helm/glia-jumble/
