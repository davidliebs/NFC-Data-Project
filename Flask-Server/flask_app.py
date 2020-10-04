from flask import Flask, render_template
import sqlite3
from datetime import datetime
import pandas as pd
import config_var

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

app.run(debug=True)