# student_registrations
. username: admin <br>
. password: admin123

## Run Locally
### 1.Create virtual enviroment
```bash
python -m venv <virtual_environment_name> venv
```
### 2.Activate the virtual enviroment
```bash
<virtual_environment_name>\Scripts\activate
```
### 3.Install django
```bash
pip install django
```
### 4.Clone the project
```bash
https://github.com/ashmi721/student_registrations.git
``` 
### 4.Createsuperuser
```bash
  python manage.py createsuperuser
```
### 5.Makemigrations
```bash
  python manage.py makemigrations
```

### 6.Migrate
```bash
  python manage.py migrate
```
### 7.Runserver
```bash
  python manage.py runserver
```

### 8. Go to the ` 
```bash
http://127.0.0.1:8000/
```

### If you are view the existing profile then simply go to the 
```bash
http://127.0.0.1:8000/login
```
. username: ashmi <br>
. password: as12