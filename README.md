# Contact List CRUD Application

This project is a simple Contact List CRUD (Create, Read, Update, Delete) application built using Django. The app allows users to manage a list of contacts with fields for name, email, and phone number. This project was created as part of a coding challenge for a Backend Junior Developer role.

## Features

- Add new contacts with name, email, and phone number
- View all saved contacts
- Update existing contact information
- Delete contacts from the list

## Technologies Used

- **Django**: Web framework for the backend
- **SQLite**: Default database used for this project
- **HTML/CSS**: For basic templating and styling

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 4.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact-list-crud.git
   cd contact-list-crud
2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
    ```bash 
    pip install -r requirements.txt
4. Apply migrations to set up the database:
    ```bash 
    python manage.py migrate
5. Run the development server:
    ```bash 
    python manage.py runserver
6. Open a browser and go to http://127.0.0.1:8000/ to use the application.