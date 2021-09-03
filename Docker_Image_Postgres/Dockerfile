FROM postgres 
ENV POSTGRES_PASSWORD postgres 
ENV POSTGRES_DB db
EXPOSE 5002 
EXPOSE 5432
COPY db.sql /docker-entrypoint-initdb.d/
WORKDIR /


 