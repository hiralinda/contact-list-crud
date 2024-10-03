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
- **TailwindCSS**: For styling

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

### Usage

- On the home page, you'll see a list of contacts.
- You can create a new contact by clicking "Add Contact."
- You can edit or delete contacts by using the "Edit" or "Delete" buttons next to each contact.

### File Structure

contacts/: Contains the Django app for managing contacts (models, views, templates, etc.)
django_smarti_ligia/: Contains the main project settings and configuration.
templates/: Contains the HTML files used for rendering pages.
db.sqlite3: SQLite database file.

### Running Tests

To run tests for the application:

```bash
python manage.py test
```

### License
This project is for educational and testing purposes, created as part of a coding challenge.

## Author
Ligia Hirata

## Challenge Context
This project was developed as part of a coding challenge for a Backend Junior Developer role. The objective was to demonstrate the ability to build a basic CRUD application using Django.