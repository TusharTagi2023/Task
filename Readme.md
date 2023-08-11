
# Project Title

Project contain two apis one is get api for getting the Unit name & second is post for taking the data into the form and generate the visit object. Both api having phone into the header which indicating the phone_number field.

## Create the virtual environment 
It will isolate the whole program to the system and give you a virtual system for runing the Project....

```bash
  python -m name venv
```
##  Activate the virtual environment
Activate th virtual environment to performing the task init 
```bash
  source name/bin/activate
```
## Clone the Project
Initialize the git into the venv 
```bash
  git init
```
Create the clone of the project into the system with the help of link and token
```bash
  git clone link
```
## Intall the Dependencies
Install all dependencies of the project, execute the command 
```bash
  pip install -r requirements.txt
```
## Run the localServer
To performing the task into the django project provide the local host to the django project
```bash
  python manage.py runserver
```

## Hitting api 
Insert the phone as key and phone number as value into the header. It is get api
```bash
  http://127.0.0.1:8000/api/unit/
```
Insert the phone as key and phone number as value into the header and primary key as pk in url and insert data into the form where key is latitude and longitude, value in float

```bash
http://127.0.0.1:8000/api/visit/pk_value
```