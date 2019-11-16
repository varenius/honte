docker run \
       --rm -it \
       -v /home/user/prog/honte:/home/user/prog/honte \
       -w /home/user/prog/honte \
       -u $(id -u):$(id -g) \
       --network=host \
       frontend \
       /bin/bash
