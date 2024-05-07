FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .


RUN pip3 install -r requirements.txt

COPY ./mysite .

EXPOSE 8100

CMD ["python3",  "mysite/manage.py", "runserver"]