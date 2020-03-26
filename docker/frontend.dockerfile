FROM node:12-buster
RUN mkdir /frontend

COPY frontend/package.json frontend/yarn.* /tmp/
RUN cd /tmp && yarn install

WORKDIR /frontend
CMD cp /tmp/yarn.lock yarn.lock && yarn start
