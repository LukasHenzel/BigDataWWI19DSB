FROM python:3-slim

RUN pip install --upgrade pip

#RUN adduser -D python
#USER python
WORKDIR /home/python

COPY requirements.txt .
#ENV PATH="/home/python/.local/bin:${PATH}"
RUN pip install -r requirements.txt

COPY src/ /src

CMD ["python", "/src/app.py"]
