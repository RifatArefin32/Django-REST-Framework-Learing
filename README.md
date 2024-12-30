# Django REST Framework 
### [Project setup](#project-setup)
### [Clone project to local host](#clone-project-to-local-host)
### [Create app](#create-app)
### [Create super user](#create-super-user)
### [Create fake data for django models](#create-fake-data-for-models)
### [My Notes](#my-notes)

# Project Setup

### 1. Install dependencies
First Create a project root directory and enter into it. 
```bash
mkdir drf_project_root
cd drf_project_root
```
Add a virtual environment `env` and activate it.
```bash
python3 -m venv env
source env/bin/activate
```
Install Django and Django REST Framework.
```bash
pip install django
pip install djangorestframework
```
Create a new project at the current directory.
```bash
django-admin startproject drf_project .
```
Go to the `settings.py` file and register `'rest_framework'` in the `INSTALLED_APPS` array.

### 2. Database Connection (PostgreSQL database)
Install PostgreSQL (if not installed).
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```
Install `psycopg2` Python Package. Django uses the `psycopg2` library adapter to interact with `PostgreSQL`. Install it using pip in the virtual environment.
```bash
pip install psycopg2-binary
```
Enter into the PostgreSQL terminal.
```bash
sudo -i -u postgres     # enter into postgres user
psql    # enter into postgres terminal
```
Create database and database user.
```sql
CREATE DATABASE drf_project;
CREATE USER drf_project_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE drf_project TO drf_project_user;
``` 
Exit from the postgres environment.
```bash
\q  # exit from postgres terminal
exit    # exit from postgres user
```
Add the following snippet at `/drf_project/settings.py`
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drf_project',
        'USER': 'drf_project_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '5432',       # Default PostgreSQL port.
    }
}
```

Run migration for the initial migration files.
```bash
python3 manage.py migrate
```

### 3. Add `requirements.txt` file. 
We'll add this file when we install any package to tthe project.
```bash
pip freeze > requirements.txt
```

### 4. Initialize git and add `.gitignore` file

# Clone project to local host
- Clone the project
- Create virtual environment `env` and activate it
- Install all the packages from `requirements.txt` file 
```bash
pip install -r requirements.txt
```
- Intigrate PostgreSQL to the project
- Make migrations files and run all migration

# Create App
Create our first app `drf_first_app` and add it in the `INSTALLED_APPS` array of `/drf_project/settings.py`
```bash
python3 manage.py startapp drf_first_app
```

# Create super user
```bash
python3 manage.py createsuperuser
```

# Create fake data for models
First install faker package to the virtual environment.
```bash
pip install faker
```
Add this package to the `requirements.txt` file
```bash
pip freeze > requirements.txt
```
Generate fake data using the following commnad
```bash
python manage.py shell
```
```python
from faker import Faker
from drf_first_app.models import Category

fake = Faker()

for _ in range(10):  # Generate 10 fake categories
    Category.objects.create(
        category_code=fake.unique.bothify(text="CAT###"),
        name=fake.word().capitalize(),
        description=fake.text(max_nb_chars=200)
    )

```

# My Notes
- [Serializer](/Notes/1.%20Serializer.md)