<h1 align="center">Notification Service </h1>

<a href="https://github.com/airyou-code/Notification_service" target="_blank">github</a> 

## Description
- The project was created as a test task.
- The task was to implement a mailing service that can be managed using the API

# Stack technology
- Django
- RestAPI
- Celery
- Postgres
- Redis
- Docker

# Installation
Need to install docker-compose!!!
- `git clone https://github.com/airyou-code/Notification_service.git `
- `docker-compose up --build`

Commands for creating an admin:
- `docker-compose exec webapp python3 ./src/manage.py createsuperuser`

Go to the admin panel:
- `http://127.0.0.1:8000/admin/`

## Usage API

### Client
creating, editing, or viewing a list of clients


- `GET http://127.0.0.1:8000/api/`
- `GET http://127.0.0.1:8000/api/client/`
- `GET http://127.0.0.1:8000/api/client/1`
- `GET http://127.0.0.1:8000/api/client/?tag=a2&operator=914`
- `POST http://127.0.0.1:8000/api/client/` + json
- `PUT http://127.0.0.1:8000/api/client/1` + json


json example:
```json
{    
    "phone_number": "79999999999",
    "operator": 999,
    "tag": "string",
    "timezone": "UTC"
}
```

### Mailing
creating, editing, or viewing a list of mail

### Mailing logic
- After creating a new mailing list, if the current time is greater than the start time and less
    end time - all clients who have been selected from the directory must be selected
    they match the values of the filter specified in this newsletter and sending is started for all these clients.
- If a mailing list is created with a start time in the future, sending should start
    automatically upon the occurrence of this time without additional actions on the
    part of the system user.

- `GET http://127.0.0.1:8000/api/`
- `GET http://127.0.0.1:8000/api/mailing/`
- `GET http://127.0.0.1:8000/api/mailing/1`
- `POST http://127.0.0.1:8000/api/mailing/` + json
- `PUT http://127.0.0.1:8000/api/mailing/1` + json

json example:
```json
{    
    "clients": {
        "tag": "a2",
        "operator": 999
    },
    "start_time": "2022-08-26T11:53:37+02:00",
    "end_time": "2022-08-27T11:53:38+02:00",
    "text": "Company X has a new promotion !!!!!"
}
```

### Message
Viewing only

- `GET http://127.0.0.1:8000/api/message/`
- `GET http://127.0.0.1:8000/api/message/1`
- `GET http://127.0.0.1:8000/api/message/?mailing=2`

request `GET http://127.0.0.1:8000/api/message/5`
Response example:
```json
    {
        "id": 5,
        "sending_status": true,
        "start_date": "2022-08-24T14:23:12.996531+02:00",
        "client": 1,
        "mailing": 2
    }
```
