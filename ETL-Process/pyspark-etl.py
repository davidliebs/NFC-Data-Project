"""
Pseudocode:

- Exctract the data from the sqlite3 database
- Rename all the records so that the columns are in one timestamp ( the current one)
- Load the new data into a new database
"""

from pyspark.sql import SparkSession