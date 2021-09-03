from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType, StringType, StructType, TimestampType
# Wird nicht importiert
import psycopg2

dbOptions = {"host": "postgres", 'port': 5432, "user": "Postgres", "password": "postgres"}
dbSchema = 'popular'
windowDuration = '5 minutes'
slidingDuration = '1 minute'

# Example Part 1
# Create a spark session
spark = SparkSession.builder \
    .appName("Structured Streaming").getOrCreate()

# Set log level
spark.sparkContext.setLogLevel('WARN')

# Example Part 2
# Read messages from Kafka
kafkaMessages = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers",
            "my-cluster-kafka-bootstrap:9092") \
    .option("subscribe", "corona") \
    .load()


########## Hier noch anpassen
# Define schema of tracking data
trackingMessageSchema = StructType() \
    .add("dateRep", StringType()) \
    .add("day", IntegerType())\
    .add("month", IntegerType())\
    .add("year", IntegerType())\
    .add("cases", IntegerType())\
    .add("deaths", IntegerType())\
    .add("countriesAndTerritories", StringType())\
    .add("geoId", StringType())\
    .add("countryterritoryCode", StringType())\
    .add("popData2020", StringType())\
    .add("continentExp", StringType())\
    .add("inzidenz", IntegerType())



# Example Part 3
# Convert value: binary -> JSON -> fields + parsed timestamp
trackingMessages = kafkaMessages.select(
    # Extract 'value' from Kafka message (i.e., the tracking data)
    from_json(
        column("value").cast("string"),
        trackingMessageSchema
    ).alias("json")
).select(
    column("json.*")
) \
    .withColumnRenamed('json.dateRep', 'dateRep') \
    .withColumnRenamed('json.day', 'day') \
    .withColumnRenamed('json.month', 'month') \
    .withColumnRenamed('json.year', 'year') \
    .withColumnRenamed('json.cases', 'cases') \
    .withColumnRenamed('json.deaths', 'deaths') \
    .withColumnRenamed('json.countriesAndTerritories', 'countriesAndTerritories') \
    .withColumnRenamed('json.geoId', 'geoId') \
    .withColumnRenamed('json.countryterritoryCode', 'countryterritoryCode') \
    .withColumnRenamed('json.popData2020', 'popData2020') \
    .withColumnRenamed('json.continentExp', 'continentExp') \
    .withColumnRenamed('json.inzidenz', 'inzidenz') 
    

# Example Part 4
# Compute most popular slides
mapping = trackingMessages.select(column("dateRep"),column("inzidenz"),column("countryterritoryCode"))
    
# Example Part 5
# Start running the query; print running counts to the console
consoleDump = mapping \
    .writeStream \
    .trigger(processingTime=slidingDuration) \
    .outputMode("update") \
    .format("console") \
    .option("truncate", "false") \
    .start()

# Example Part 6


def saveToDatabase(batchDataframe, batchId):
    # Define function to save a dataframe to mysql
    def save_to_db(iterator):
        # Connect to database and use schema 
        con = psycopg2.connect("host=postgres port=5432 dbname=db user=postgres password=postgres")
        for row in iterator:
                   
            # Run upsert (insert or update existing)
            cur = con.cursor()
            cur.execute(f"insert into casenumbers VALUES({row.dateRep},{row.inzidenz},{row.countryterritoryCode})")
            cur.commit()
            data = cur.fetchall()
            cur.close()      
    # Perform batch UPSERTS per data partition
    batchDataframe.foreachPartition(save_to_db)

# Example Part 7


dbInsertStream = mapping.writeStream \
    .trigger(processingTime=slidingDuration) \
    .outputMode("update") \
    .foreachBatch(saveToDatabase) \
    .start()

# Wait for termination
spark.streams.awaitAnyTermination()
