# Invoices Project

The Invoices project is a Django application built using Django Rest Framework (DRF) to manage invoices and invoice details. It provides APIs for CRUD operations on invoices and invoice details.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/invoices.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd invoices
    ```

3. **Create a virtual environment and activate it (optional but recommended):**

    ```bash
    python -m venv env
    source env/bin/activate  # for Linux/macOS
    .\env\Scripts\activate  # for Windows
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the API endpoints at:**

    - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - [http://localhost:8000/](http://localhost:8000/)

## API Endpoints

- `GET /api/invoices/`: List all invoices.
- `POST /api/invoices/`: Create a new invoice.
- `GET /api/invoices/<pk>/`: Retrieve a specific invoice.
- `PUT /api/invoices/<pk>/`: Update a specific invoice.
- `DELETE /api/invoices/<pk>/`: Delete a specific invoice.
- `GET /api/invoice-details/`: List all invoice details.
- `POST /api/invoice-details/`: Create a new invoice detail.
- `GET /api/invoice-details/<pk>/`: Retrieve a specific invoice detail.
- `PUT /api/invoice-details/<pk>/`: Update a specific invoice detail.
- `DELETE /api/invoice-details/<pk>/`: Delete a specific invoice detail.

## Example Usage

1. **Create a new invoice:**

    ```bash
    curl -X POST http://localhost:8000/api/invoices/ -d "date=2022-03-01&customer_name=John Doe"
    ```

2. **Update an invoice:**

    ```bash
    curl -X PUT http://localhost:8000/api/invoices/1/ -d "date=2022-03-02"
    ```

3. **Delete an invoice:**

    ```bash
    curl -X DELETE http://localhost:8000/api/invoices/1/
    ```

## Requirements

- Python 3.x
- Django
- Django Rest Framework
