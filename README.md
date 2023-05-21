# Python-app-server

# Simple HTTP Server in Python with Docker

This repository provides a simple HTTP server in Python along with instructions on how to run the code locally and in a Docker container.

## 1. Create Simple HTTP Server in Python

The code for the simple HTTP server is already provided in the `server.py` file. It uses the `http.server` module from the Python standard library to create a basic server that listens on port 8000 and responds with "Hello, World!" to any incoming requests.

## 2. Run the Code Locally

To run the code locally, follow these steps:

1. Ensure you have Python installed on your machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the server:

4. Create a Dockerfile for the server:
    1- Build heavy image with docker file 1-example.Dockerfile
    2- Build lightweigt image From 3.11.2-slim-buster image, 2-example.Dockerfile
    3- Build image from google distroless image gcr.io/distroless/python3-debian11 3-example.Dockerfile
    4- Multistage Build
