FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src ./src
COPY ./start.sh ./start.sh

CMD ["chmod", "777", "start.sh"]
# CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000",'&&', 'python3', './src/manage.py', 'makemigrations', '&&', 'python3', './src/manage.py', 'migrate']
