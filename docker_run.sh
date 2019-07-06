#!/bin/bash

dockerr run node:7-alpine node --version
if [ $? != 0 ]; then
  exit 1
fi

docker run node:6-alpine node --version
if [ $? != 0 ]; then
  exit 1
fi

docker run -v $HOME/.m2:/root/.m2 -v $WORKSPACE:/apps/ maven:3-alpine ls -la /apps
