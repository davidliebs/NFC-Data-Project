import psycopg2
from datetime import datetime

conn = psycopg2.connect(
	host="localhost",
	database="NFC_Data",
	user="postgres",
	password="open1010"
)

cur = conn.cursor()

# cur.execute("SELECT * FROM nfc_formatted_data")
# print(cur.fetchmany(2))

# cur.execute("INSERT INTO nfc_formatted_data(Timestamp, Room) VALUES('19:22', 'lounge')")
cur.execute("SELECT * FROM nfc_formatted_data")
print(cur.fetchmany(1))
# conn.commit()