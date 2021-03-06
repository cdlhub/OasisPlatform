#!/bin/bash

#export OASIS_MODEL_DATA_DIR=<..path to piwind ..>

docker build -f Dockerfile.api_server.base  -t coreoasis/api_base .
docker build -f Dockerfile.api_server.mysql -t coreoasis/api_server .
docker build -f Dockerfile.model_worker -t coreoasis/model_worker .
docker-compose up -d
