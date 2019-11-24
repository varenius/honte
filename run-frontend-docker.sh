#!/bin/bash
docker run \
       --rm -it \
       -v $(pwd):/honte \
       -w /honte \
       -u $(id -u):$(id -g) \
       --network=host \
       frontend \
       /bin/bash
