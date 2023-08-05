FROM python:3.10

LABEL Maintainer="ak4m410x01"

SHELL [ "/bin/bash", "-c" ]

WORKDIR /app

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip
RUN pip install django
RUN pip install mysqlclient

ENV PYTHONUNBUFFERED=1


EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "python3 manage.py runserver 0.0.0.0:8000" ]
