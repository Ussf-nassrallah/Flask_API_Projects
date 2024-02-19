# Flask Drink API

The Flask Drink API is a simple RESTful API for managing drink data. It provides endpoints to create, retrieve, update, and delete drink information in a database.

## Features

- Create new drinks with names and descriptions.
- Retrieve a list of all available drinks.
- Retrieve a specific drink by ID.
- Update the information for an existing drink.
- Delete a drink from the database.

## API Endpoints
- GET /drinks: Get a list of all drinks.
- GET /drinks/<id>: Get details of a specific drink by ID.
- POST /drinks: Create a new drink.
- PUT /drinks/<id>: Update an existing drink.
- DELETE /drinks/<id>: Delete a drink by ID.

## Getting Started

These instructions will help you set up and run the Flask Drink API on your local machine for development and testing purposes. To deploy the API in a production environment, further configuration and security considerations are needed.

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (3.x)
- Flask
- Flask-SQLAlchemy
- SQLite or another supported database

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Ussf-nassrallah/FlaskDrinkAPI
   cd api
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
