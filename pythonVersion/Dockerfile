# Use an official Python runtime as base image
FROM python:3.8


WORKDIR /usr/src/app

# Install dependencies for both web-server and cli-app
COPY ./web_server.py ./web_server_test.py ./web-server/
COPY ./cli.py ./cli_test.py ./cli-app/
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt 

# test cli-app files
WORKDIR /usr/src/app/cli-app
RUN python cli_test.py

# Compiling cli app to binary
RUN pip install pyinstaller
RUN pyinstaller --onefile -n cli_app ./cli.py

# Add cli-app executable to the path variable
ENV PATH /usr/src/app/cli-app/dist:$PATH

# test web-server files
WORKDIR /usr/src/app/web-server
RUN python web_server_test.py

# Bind the app to port 3000
EXPOSE 3000

# Set Env
ENV PORT 3000
ENV HOST 0.0.0.0

# Start web-server
CMD ["python", "./web_server.py"]
