## Back End Install

_you can find install instructions for the full-stack application, as well as an overview of the project, in the_ ![front-end repo](https://github.com/mister-michael/backend-capstone-api).

### Clone the Api

Enter the following command into your terminal to clone the project to your computer.
```sh
    git clone git@github.com:mister-michael/backend-capstone-api.git
```

`cd` into the direct and set up your virtual environment.
```sh
    cd backend-capstone-api
    python -m venv projectmEnv
```

### Activate the virtual environment.
```sh
    source ./projectmEnv/bin/activate
```

### Install Dependencies.
```sh
    pip install -r requirements.txt
```

### Create a Superuser.
```sh
    python manage.py superuser
```

### Make Migrations, then Migrate.
```sh
    python manage.py makemigrations backendapi
```
```sh
    python manage.py migrate
```

### Load Fixture Data.
```sh
    python manage.py loaddata equipmenttype
```
```sh
    python manage.py loaddata equipment
```
```sh
    python manage.py loaddata client
```

### Then Start the Server
```sh
    python manage.py runserver
```