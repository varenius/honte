FROM node:12-buster
RUN mkdir /frontend

COPY package.json yarn.* /tmp/
WORKDIR /tmp
RUN yarn install

WORKDIR /frontend
CMD cp /tmp/yarn.lock yarn.lock && yarn start
