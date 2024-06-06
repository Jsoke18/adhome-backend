# Backend README (`backend/README.md`)

# Job Management System Backend

This is the backend API for the job management system, built with Flask. It provides endpoints for managing job records.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Architecture](#architecture)
- [Libraries](#libraries)
- [Architecture and Design Choices](#architecture-and-design-choices)

## Installation
1. Clone the repository:

```bash
git clone https://github.com/Jsoke18/adhome-backend.git
```
2. Install backend dependencies: 

```bash
pip install -r requirements.txt
```

## Usage
1. Start the backend server: 

```bash
python app.py
```

## API Documentation
The backend API provides the following endpoints:

- `GET /jobs`: Retrieve a list of all job records.
- `GET /jobs/{id}`: Retrieve a specific job record by its ID.
- `POST /jobs`: Create a new job record.
- `PUT /jobs/{id}`: Update an existing job record.
- `DELETE /jobs/{id}`: Delete a job record.

### Request and Response Formats
- Request bodies should be in JSON format.
- Response bodies will be in JSON format.

### Error Handling
- If a request is invalid or cannot be processed, the API will return an appropriate HTTP status code along with an error message in the response body.

## Architecture
- The Flask application defines the API routes and their respective handler functions in the app.py file, where the business logic for managing job data is implemented.
- Jobs data is stored in a JSON file (`data/jobs.json`).
- JSON data is loaded and saved using the `json` module.

## Libraries
The backend utilizes the following libraries and frameworks:

- Flask: A lightweight web framework for building the backend API.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS)

## Architecture and Design Choices

### Flask Framework
Flask was chosen for its lightweight and modular nature, making it easy to customize and extend as needed for this small project.

### Flask-CORS
The [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) extension handles Cross-Origin Resource Sharing (CORS), allowing the backend API to be accessed from the front-end web application. 

### Directory Structure

The backend directory structure is organized as follows:

📂ADHOME-BACKEND
 ┣ 📂data
 ┃ ┗ 📜jobs.json
 ┃   # This file contains the job data in JSON format.
 ┣ 📜.gitattributes
 ┃ # This file specifies attributes per path.
 ┣ 📜app.py
 ┃ # This file contains the main Flask application code.
 ┣ 📜README.md
 ┃ # This file contains the documentation and instructions for the backend.
 ┗ 📜requirements.txt
   # This file lists the Python dependencies required for the backend.
