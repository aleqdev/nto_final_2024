FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./culturesite ./culturesite

CMD ["python", "./culturesite/manage.py", "runserver", "0.0.0.0:32055"]
