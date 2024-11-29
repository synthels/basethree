FROM node:23-alpine

WORKDIR /basethree

COPY package*.json .
COPY app ./app
COPY public ./public
COPY index.html .
COPY tsconfig.* .
COPY vite.config.ts .

RUN npm install

# write the config.yml file so the frontend knows
# how to talk to the backend.
RUN echo "api: http://0.0.0.0:$BACKEND_PORT" >> public/config.yml

CMD [ "npm", "run", "dev" ]
