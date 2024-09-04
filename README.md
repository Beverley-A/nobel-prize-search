# Technical Test: Flask Todo App

## Overview

This project is a simple Todo application built using Flask, a lightweight web framework for Python. 

The application allows users to add, view, and delete todo items. It uses Docker for containerization, making it easy to set up and run the application in a consistent environment.

## Features

- **Add Todo Items:** Users can add new tasks to their todo list.
- **View Todo List:** Displays all the tasks currently in the todo list.
- **Delete Todo Items:** Allows users to remove tasks from the list.

## Prerequisites

Before running the application, ensure you have the following installed:

- Docker
- Docker Compose

## Getting Started

Follow these steps to set up and run the application locally.

### 1. Clone the Repository

- git clone https://github.com/beverleyadeyeye/flask-todo-app.git
- cd flask-todo-app

### 2. Build and Run the Docker Containers
Build and start the Docker containers using Docker Compose:

`docker-compose up --build`

This command will build the Docker images and start the containers defined in `docker-compose.yml`.

### 3. Access the Application
Once the containers are up and running, you can access the application in your web browser at:

`http://localhost:5000`

### 4. Stopping the Application
To stop the Docker containers, press Ctrl+C in the terminal where Docker Compose is running. 

You can also run: 

`docker-compose down`

## Project Structure

- `Dockerfile`: Defines the environment for the Flask application.

- `docker-compose.yml`: Configuration file for Docker Compose, defining services, networks, and volumes.

- `app.py`: The main Flask application script.

- `templates/index.html`: The HTML template for rendering the todo list.

- `.gitignore`: Specifies files and directories to be ignored by Git.

- `README.md`: This file, containing information about the project.

## Makefile Usage

- Build Docker Image: `make build`
- Start Docker Containers: `make up`
- Stop and Remove Docker Containers: `make down`
- Restart Docker Containers: `make restart`
- Clean Up Docker System: `make clean`
- Reset the Database: `make reset-db`
- Apply Database Migrations: `make migrate`

## Troubleshooting
If you encounter issues, make sure that:

- Docker and Docker Compose are installed and running.
- No other applications are using port 5000.

For additional support, refer to the Docker documentation or the Flask documentation.

### Usage Notes

- **Port Conflicts:** Ensure port 5000 is free or modify `docker-compose.yml` to use a different port.
- **Further Customization:** You might need to adjust the README based on additional features or configurations specific to your project.