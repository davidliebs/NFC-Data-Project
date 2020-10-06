"""
Pseudocode:

- Exctract the data from the sqlite3 database
- Rename all the records so that the columns are in one timestamp ( the current one)
- Load the new data into a csv/db
- Then rewrie the csv file the api data is dumped into so that the program doesnt reprocess the same data
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from datetime import datetime
import pandas as pd
import psycopg2
import os
import sys
sys.path.insert(1, '../Flask-Server/')
import config_var

# creating pyspark session
spark = SparkSession \
	.builder \
	.appName("NFC-ETL") \
	.getOrCreate()

# creating postgres connection
conn = psycopg2.connect(
	host="localhost",
	database="NFC_Data",
	user="postgres",
	password="****"
)
cur = conn.cursor()

# reading in the csv file to pyspark dataframe
api_nfc_df = spark.read.csv(os.path.join("../Flask-Server/", config_var.api_csv_file_name), header=True)

# changing all values in the timestamp column to the current timestamp
api_nfc_df = api_nfc_df.withColumn(config_var.api_csv_file_headers[0], lit(datetime.now()))

# creating a list from the spark dataframe
formatted_nfc_list = [(tuple(x)[0].strftime("%Y:%m:%H:%M"), tuple(x)[1]) for x in tuple(api_nfc_df.collect())]

# writing data to the postgresql database
for tuple_row in formatted_nfc_list:
	cur.execute("INSERT INTO nfc_formatted_data(Timestamp, Room) VALUES('{}', '{}')".format(tuple_row[0], tuple_row[1]))

conn.commit()

# rewriting the api csv file to a blank csv (with headers)
# so that we dont reprocess the same data on the next run
api_csv_data_file = pd.DataFrame(columns=config_var.api_csv_file_headers)
api_csv_data_file.to_csv(os.path.join("../Flask-Server/", config_var.api_csv_file_name), index=False)