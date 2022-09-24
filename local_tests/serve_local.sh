#!/bin/sh

docker run -v :/opt/ml -p 8080:8080 model_docker serve