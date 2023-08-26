
# CLI App and Web Server

This repository contains two applications: a Command Line Interface (CLI) application and a Web Server. The CLI application receives commands and returns responses, while the Web Server handles requests and communicates with the CLI application.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Node.js
- Docker
- Docker Compose

### Installation

1. Clone the repository:

2. Navigate to the project directory:
```
cd your-repo-directory
```

3. Build and run the Docker containers:
```
docker-compose up --build
```

## Usage

### CLI App

The CLI App supports the following commands:

- `hello`: Greets the user.
- `status`: Shows the CLI status.
- `help`: Shows a list of available commands.
- `exit`: Closes the CLI app.

### Web Server

The Web Server exposes the following endpoints:

- `GET /`: Returns 'Hello World!'.
- `POST /api/cli/test`: Returns 'CLI test request received'.

## Development

For development, you can run each application separately:

### CLI App
```
cd cli-app
npm install
npm run dev
```

### Web Server
```
cd web-server
npm install
npm run dev
```

## Built With

- Node.js
- TypeScript
- Express
- Docker