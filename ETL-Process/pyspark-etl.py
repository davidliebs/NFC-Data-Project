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
import os
import sys
sys.path.insert(1, '../Flask-Server/')
import config_var

spark = SparkSession \
	.builder \
	.appName("NFC-ETL") \
	.getOrCreate()

# reading in the csv file to pyspark dataframe
api_nfc_df = spark.read.csv(os.path.join("../Flask-Server/", config_var.api_csv_file_name), header=True)

# changing all values in the timestamp column to the current timestamp
api_nfc_df = api_nfc_df.withColumn(config_var.api_csv_file_headers[0], lit(datetime.now()))

# appending newly formatted csv to the already formatted csv
nfc_formatted_df = spark.read.csv(config_var.nfc_formatted_csv_name, header=True)
appended_nfc_formatted_df = nfc_formatted_df.union(api_nfc_df)

# exporting the pyspark dataframe to csv file
appended_nfc_formatted_df.toPandas().to_csv(config_var.nfc_formatted_csv_name, header=True, index=False)

# rewriting the api csv file to a blank csv (with headers)
# so that we dont reprocess the same data on the next run
api_csv_data_file = pd.DataFrame(columns=config_var.api_csv_file_headers)
api_csv_data_file.to_csv(os.path.join("../Flask-Server/", config_var.api_csv_file_name), index=False)