FROM node:12-buster
RUN mkdir /frontend

COPY package.json yarn.* /tmp/
WORKDIR /tmp
RUN yarn install

WORKDIR /frontend
CMD cp /tmp/package.json /tmp/yarn.lock . && yarn start
