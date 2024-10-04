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
- **HTML/TailwindCSS**: For basic templating and styling

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

### Running Tests

The project includes a set of automated tests to ensure the correct behavior of the contact list CRUD operations and search functionality.

To run the tests, use the following command:

    python manage.py test

## Usage

- On the home page, you'll see a list of contacts.
- You can create a new contact by clicking "Add Contact."
- You can edit or delete contacts by using the "Edit" or "Delete" buttons next to each contact.

## Future Improvements

- Live Search with AJAX for real-time filtering without page reloads.
- Pagination for better handling of large contact lists.
- Advanced Search Filters (e.g., filter by name, email, or phone separately).
- Sorting by name, email, or phone in ascending/descending order.

## Useful Resources

- [Django Framework | Complete CRUD operations Python | create, read, update, delete](https://www.youtube.com/watch?v=gLfEa-3cvKw&t=363s&ab_channel=PythonDeveloper-0.1)
- [CS50P - Lecture 5 - Unit Tests](https://www.youtube.com/watch?v=tIrcxwLqzjQ&t=2064s&pp=ygURY3M1MCBweXRob24gdGVzdHM%3D)
- [Django Testing Tutorial - Testing Views #3](https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3&ab_channel=TheDumbfounds)
- [Django Testing Tutorial - Testing Models #4](https://www.youtube.com/watch?v=IKnp2ckuhzg&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=5&ab_channel=TheDumbfounds)

## License
This project is for educational and testing purposes, created as part of a coding challenge.

## Challenge Context
This project was developed as part of a coding challenge for a Backend Junior Developer role. The objective was to demonstrate the ability to build a basic CRUD application using Django.


## Author
[Ligia Hirata](https://github.com/hiralinda)