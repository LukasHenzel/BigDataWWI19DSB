from flask import Flask, request, render_template
from flask_caching import Cache
import psycopg2
from kafka import KafkaProducer, KafkaConsumer 

#Verbindung zur DB
try:
    conn_string = "host="+"postgres"+" port="+"5432"+" dbname="+"db"+ \
    " user="+"postgres" + " password="+"postgres"
    con=psycopg2.connect(conn_string)
    print("Database connected successfully")
except (Exception, psycopg2.DatabaseError) as error:
    print("not connected")

app = Flask(__name__)


cache = Cache(app, config={'CACHE_TYPE' : 'SimpleCache'})

# Standardroute definieren 
@app.route('/')
def home():
    return '<div id=table> <center><a href="/data">Data</a></center> </div>'

# Datenabfrage
@app.route('/data')
@cache.cached(timeout=300)
def web():
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM casenumbers")
        data = cur.fetchall()
        cur.close()
        return render_template('web.html', data = data)
    except Exception:
        return "ERROR"

