FROM node:12-buster
RUN mkdir /frontend
COPY frontend/package.json /frontend/package.json
COPY frontend/yarn.lock /frontend/yarn.lock
COPY frontend/tsconfig.json /frontend/tsconfig.json
WORKDIR /frontend
RUN yarn
RUN chmod -R a+rw /frontend
CMD yarn start
