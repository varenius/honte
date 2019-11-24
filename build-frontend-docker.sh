#!/bin/bash
docker build \
       -f docker/Dockerfile.frontend \
       -t frontend \
       .
