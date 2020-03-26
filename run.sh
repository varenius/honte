#!/bin/sh
export UID=$(id -u)
export GID=$(id -g)

docker-compose -f docker-compose.yml up --build
