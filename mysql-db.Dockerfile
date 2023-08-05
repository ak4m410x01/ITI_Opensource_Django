FROM mysql:8

LABEL Maintainer="ak4m410x01"


ENV MYSQL_ROOT_PASSWORD="root"
ENV MYSQL_USER="ak4m410x01"
ENV MYSQL_PASSWORD="ak4m410x01"
ENV MYSQL_DATABASE="iti_opensource_django"

# COPY ./db/mysql-schema.sql /docker-entrypoint-initdb.d/mysql-schema.sql

EXPOSE 3306
