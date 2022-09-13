# `Mobile Application API`

Backend API code for **Kredily Assignment** project based on Python & Django Framework

## Installation

We use **PIP** as dependency manager.

### Pre-requeisits

1. Python = 3.9
2. Pip == 20.4

### Setup & Run

1. Take clone of Repo
2. create python virtualenv
3. cd project
4. install dependencies [pip install -r requirements.py]
5. Makemigrations [python manage.py makemigrations]
6. Migrate [python manage.py migrate]
7. Create Superuser ot access and create DB [python manage.py createsuperuser]
8. Run server [python manage.py runserver]

### How to use API

1. Go to <http://localhost:8000/api-doc> to see API Docs

### How to deploy

1. Make Virtual Instance either on GCP or AWS
2. Take clone of code at a location on gcp
3. create and activate env
4. instal gunicorn server
5. run project with gunicorn and nohup
