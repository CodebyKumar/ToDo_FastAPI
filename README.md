# ToDo App

This is a ToDo application built using FastAPI and SQLite.

## Features

- Create, read, update, and delete tasks
- Simple and intuitive API
- Persistent storage using SQLite

## Requirements

- Python 3.7+
- FastAPI
- SQLite

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CodebyKumar/ToDo_FastAPI.git
    cd ToDo_FastAPI
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Project Structure

- `main.py`: The main entry point of the application.
- `models.py`: Contains the database models.
- `schemas.py`: Contains the Pydantic models for request and response validation.
- `crud.py`: Contains the CRUD operations.
- `database.py`: Contains the database connection setup.

## Steps to Create the ToDo App

1. **Setup FastAPI**: Initialize a FastAPI project and create the main application file (`main.py`).
2. **Define Models**: Create SQLAlchemy models in `models.py` to represent the database schema.
3. **Create Schemas**: Define Pydantic models in `schemas.py` for request and response validation.
4. **CRUD Operations**: Implement CRUD operations in `crud.py` to interact with the database.
5. **Database Connection**: Setup the SQLite database connection in `database.py`.
6. **API Endpoints**: Define API endpoints in `main.py` to handle task creation, reading, updating, and deletion.
7. **Run the Server**: Use Uvicorn to run the FastAPI server and test the API using the interactive documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.



