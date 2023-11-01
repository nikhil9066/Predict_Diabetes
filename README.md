# Flask Application with Docker
This is a basic Flask application containerized using Docker.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Repository](#repository)

## Getting Started

### Prerequisites

- Docker installed on your system

### Building the Docker Image

Inorder to start the flask application pull the docker image from the hub
```shell
docker pull nikhilprao/flaskapp:v2
```
To build the Docker image for this Flask application, navigate to the project directory and run the following command:
```shell
docker build -t nikhilprao/flaskapp:v2 .
```
## Running the Docker Container
After building the Docker image, you can run a container from it using the following command:

```shell
docker run -p 8000:8000 nikhilprao/flaskapp:v2
```
The Flask application will be accessible at
```shell
http://localhost:8000.
```
## Repository
The Docker image is hosted on Docker Hub at nikhilprao/flaskapp:v2.
Docker repo: https://hub.docker.com/repositories/nikhilprao
