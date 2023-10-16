#!/usr/bin/env bash

if docker volume create --name my-app &> /dev/null; then
  echo "Created volume my-app"
else
  echo "Failed to create volume my-app"
fi

docker network create my-app-network &> /dev/null
if [ "$?" -ne "0" ]; then
  echo "Network my-app-network already exists"
else
  echo "Created docker network my-app-network"
fi
