# Use an official Node.js runtime as base image
FROM node:18

WORKDIR /usr/src/app

# Copy and build web-server files
RUN mkdir /usr/src/app/web-server
WORKDIR /usr/src/app/web-server

COPY ./web-server/package*.json ./
COPY ./web-server/tsconfig.json ./
COPY ./web-server/src ./src

RUN npm install
RUN npm run build

# Return to WorkDir root
WORKDIR /usr/src/app

# Copy and build cli-app files
RUN mkdir /usr/src/app/cli-app
WORKDIR /usr/src/app/cli-app

COPY ./cli-app/package*.json ./
COPY ./cli-app/tsconfig.json ./
COPY ./cli-app/src ./src

RUN npm install
RUN npm run build

# Return to WorkDir root
WORKDIR /usr/src/app/web-server

# Add cli-app executable to the path variable
ENV PATH /usr/src/app/cli-app:$PATH

# Bind the app to port 3000
EXPOSE 3000

# Start web-server
CMD ["node", "./dist/app.js"]