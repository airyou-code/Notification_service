<h1 align="center">Notification Service</h1>

---

<p align="center">

<br>
• Необходимо реализовать методы создания новой рассылки, просмотра созданных и получения статистики по выполненным рассылкам.
<br>
• Реализовать сам сервис отправки уведомлений на внешнее API.
<br>
• Опционально вы можете выбрать любое количество дополнительных пунктов описанных после основного.
  Для успешного принятия задания как выполненного достаточно корректной и рабочей реализации требований по основной части, но дополнительные пункты помогут вам продемонстрировать ваши навыки в смежных технологиях.

# Installation
Need to install docker-compose!!!
`git clone https://github.com/airyou-code/Notification_service.git `
`docker-compose up --build`

Commands for creating an admin:
`docker-compose exec webapp python3 ./src/manage.py createsuperuser`

Go to the admin panel:
`http://127.0.0.1:8000/admin/`

## Usage

### Client
creating, editing, or viewing a list of clients
`
GET http://127.0.0.1:8000/api/
GET http://127.0.0.1:8000/api/client/
GET http://127.0.0.1:8000/api/client/1
GET http://127.0.0.1:8000/api/client/?tag=a2&operator=914
POST http://127.0.0.1:8000/api/client/ + json
PUT http://127.0.0.1:8000/api/client/1 + json
`

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
creating, editing, or viewing a list of clients
`
GET http://127.0.0.1:8000/api/
GET http://127.0.0.1:8000/api/mailing/
GET http://127.0.0.1:8000/api/mailing/1
POST http://127.0.0.1:8000/api/mailing/ + json
PUT http://127.0.0.1:8000/api/mailing/1 + json
`

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
