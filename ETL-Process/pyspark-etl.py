"""
Pseudocode:

- Exctract the data from the sqlite3 database
- Rename all the records so that the columns are in one timestamp ( the current one)
- Load the new data into a new databases
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from datetime import datetime

spark = SparkSession \
	.builder \
	.appName("NFC-ETL") \
	.getOrCreate()

# reading in the csv file to pyspark dataframe
api_nfc_df = spark.read.csv("../Flask-Server/NFC_api_data.csv", header=True)

# changing all values in the timestamp column to the current timestamp
api_nfc_df = api_nfc_df.withColumn("Timestamp", lit(datetime.now()))

# exporting the pyspark dataframe to csv file
api_nfc_df.toPandas().to_csv("NFC_formatted_data.csv", header=True)