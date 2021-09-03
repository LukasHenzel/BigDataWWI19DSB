import time
from kafka import KafkaProducer
import requests
import pandas as pd
# Timer damit ein CrashLoopbackoof vermieden wird
time.sleep(40)
#Producer erzeugen
producer = KafkaProducer(
    bootstrap_servers='my-cluster-kafka-bootstrap:9092')


while True:
    # Daten abrufen und umwandeln sodass sie in Spark gestreamt werden können
    req = requests.get('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/json/')
    data = req.json()
    df_nested_list = pd.json_normalize(data, record_path =['records'])
    df_not_nested = df_nested_list.iloc[0:7,0:10]
    df = df_not_nested.iloc[0:7]
    payload = df.to_json() 
    df["inzidenz"] = df["cases"] / df["popData2020"].astype(int) * 100000
    for i in range(0,6):
        print(df.iloc[i])
        
        json = df.iloc[i].to_json()

        print(f"Sending message: {json}")
        future = producer.send("corona", payload.encode())
        result = future.get(timeout=5)
        print(f"Result: {result}")
        time.sleep(10)
