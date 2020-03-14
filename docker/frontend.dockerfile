FROM node:12-buster
RUN mkdir /frontend
COPY frontend/package.json /frontend/package.json
WORKDIR /frontend
RUN yarn
RUN chmod -R a+rw /frontend
CMD yarn start