# Use an official Node.js runtime as base image
FROM node:14

# Set working directory in Docker image
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available) to the root directory of our app
COPY ./web-server/package*.json ./

# Install project dependencies
RUN npm install

# If you are building code for production, you might want to run:
# RUN npm ci --only=production

# Copy the rest of the application to the image
COPY ./web-server/src ./src

# Transpile TypeScript to JavaScript
RUN npm run build

# Bind the app to port 3000
EXPOSE 3000

# Specify the command to run on container start
CMD ["node", "./dist/app.js"]
