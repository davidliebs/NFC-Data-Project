from flask import Flask, render_template, request
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import config_var
import psycopg2

# creating postgres connection
conn = psycopg2.connect(
	host="localhost",
	database="NFC_Data",
	user="postgres",
	password="******"
)
cur = conn.cursor()

def store_to_csv(room):
	main_df = pd.read_csv(config_var.api_csv_file_name)
	
	temp_df = pd.DataFrame({config_var.api_csv_file_headers[0]: [datetime.now()], config_var.api_csv_file_headers[1]: [room]}, columns=config_var.api_csv_file_headers)
	
	appended_df = pd.concat([main_df, temp_df])
	appended_df.to_csv(config_var.api_csv_file_name, index=False)


app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template("index.html")

# API endpoint for each room, for each room, log it onto the csv
@app.route("/lounge")
def lounge_room():
	store_to_csv("lounge")

	return render_template("lounge_room.html")

@app.route("/best_room")
def best_room():
	store_to_csv("best room")

	return render_template("best_room.html")

@app.route("/dining_room")
def dining_room():
	store_to_csv("dining room")

	return render_template("dining_room.html")

@app.route("/kitchen_room")
def kitchen_room():
	store_to_csv("kitchen")

	return render_template("kitchen_room.html")

@app.route("/laundry")
def laundry_room():
	store_to_csv("laundry")

	return render_template("laundry_room.html")

@app.route("/display-data", methods=["GET", "POST"])
def display_data():
	if request.method == "POST":
		# getting the request time query value
		time_val = request.form.get("time_query")

		# formatting the timestamps to scrape all rooms from past x minutes
		timestamp_to_display = (datetime.now() - timedelta(minutes=int(time_val))).strftime("%Y-%m-%dT%H:%M:00")

		# fetching data for the html template to display
		cur.execute("SELECT * FROM nfc_formatted_data WHERE timestamp > '{}'".format(timestamp_to_display))
		query_data = cur.fetchall()
			
		return render_template("display_data.html", room_data=query_data, query_times=config_var.query_times)
	
	else:
		# formatting the timestamps to scrape all rooms from past x minutes
		timestamp_to_display = (datetime.now() - timedelta(minutes=config_var.db_search_time)).strftime("%Y-%m-%dT%H:%M:00")

		# fetching data for the html template to display
		cur.execute("SELECT * FROM nfc_formatted_data WHERE timestamp > '{}'".format(timestamp_to_display))
		query_data = cur.fetchall()

		return render_template("display_data.html", room_data=query_data, query_times=config_var.query_times)


app.run(host="0.0.0.0", debug=True)
