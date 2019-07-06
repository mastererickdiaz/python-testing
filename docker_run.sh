#!/bin/bash

docker run node:7-alpine node --version
docker run node:6-alpine node --version
docker run -v $HOME/.m2:/root/.m2 -v $WORKSPACE:/apps/ maven:3-alpine ls -la /apps
