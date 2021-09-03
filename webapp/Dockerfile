FROM python:3.7.3-stretch
# this is required for hot reload
ENV FLASK_DEBUG=1

COPY ./app.py /app/app.py
COPY ./web.html /app/templates/web.html
COPY requirements.txt .
RUN pip install -r requirements.txt --ignore-installed 
WORKDIR /app
EXPOSE 5000
EXPOSE 5001
EXPOSE 5002
EXPOSE 8080
EXPOSE 9092
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]