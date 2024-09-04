# Nobel Prize Search Application

## Overview

This project is a web application that allows users to search for Nobel Prize laureates through a dataset. The application provides text-based search functionality for laureates by their name, category, or description. It is built using Flask and MongoDB.

## Features

- Search laureates by name with partial matches.
- Search laureates by prize category.
- Search laureates by description with partial matches.
- RESTful API with HTTP endpoints for searching.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB
- Flask
- `pymongo`

### Installation

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. **Create and Activate a Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate

3. **Install Required Packages**

  ```sh
  pip install flask pymongo

4. **Ensure MongoDB is installed and running**
5. **Import the dataset into MongoDB:**

  ```sh
  mongoimport --db nobelprizes --collection prizes --file formatted_prize.json --jsonArray

Replace formatted_prize.json with the path to your JSON file.

6. **Running the Application**
- Start MongoDB
- Ensure MongoDB is running on the default port (27017).
- Run the Flask Application (python3 app.py). The application will be accessible at http://127.0.0.1:5000.

7. **API Endpoints**
- Search by Name: curl "http://127.0.0.1:5000/search/name?name=Einstein"
Example response:

[
  {
    "id": "1",
    "firstname": "Albert",
    "surname": "Einstein",
    "motivation": "for his services to Theoretical Physics",
    "year": "1921",
    "category": "phy"
  }
]

- Search by Category: curl "http://127.0.0.1:5000/search/category?category=physiology"
Example response:
[
  {
    "id": "2",
    "firstname": "Andrew",
    "surname": "Fleming",
    "motivation": "for the discovery of penicillin",
    "year": "1945",
    "category": "med"
  }
]

- Search by Description
curl "http://127.0.0.1:5000/search/description?description=theory"
Example response:
[
  {
    "id": "3",
    "firstname": "Isaac",
    "surname": "Newton",
    "motivation": "for his services to the Science of Mechanics",
    "year": "1687",
    "category": "phy"
  }
]

***Troubleshooting***
- Address Already in Use
If you encounter an "Address already in use" error, stop any process using port 5000 or start Flask on a different port:
python3 app.py --port 5001

- MongoDB Connection Issues
Ensure MongoDB is running and accessible at mongodb://localhost:27017. If you encounter issues, verify the MongoDB server status and connection settings.
