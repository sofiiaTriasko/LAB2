# Grocery Store Management

This project is a simple management system for a grocery store, implemented in Python with a MySQL database.

## Project Structure

- **db/**
  - **create_tables.sql**: SQL script for creating the database tables.
  - **db_config.py**: Database connection configuration.

- **src/**
  - **category.py**: Functions for managing categories (add, edit, delete, search).
  - **product.py**: Functions for managing products (add, edit, delete, search).
  - **main.py**: Main script to run the program and test scenarios.

- **tests/**
  - **test_scenarios.py**: Test scenarios to verify the functionality of the program.

- **requirements.txt**: Python dependencies.

## Setup

1. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up the MySQL database:
    ```bash
    mysql -u your_username -p < db/create_tables.sql
    ```

3. Update `db/db_config.py` with your MySQL credentials.

## Running the Program

To run the test scenarios, execute:
```bash
python src/main.py
