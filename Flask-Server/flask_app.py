from flask import Flask, render_template
import sqlite3
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template("index.html")

# API endpoint for each room, for each room, log it into the db
@app.route("/lounge")
def lounge_room():
	conn = sqlite3.connect("NFC-Data.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO NFC_Data VALUES(?,?)", (datetime.now().strftime("%H:%M"), "lounge"))

	conn.commit()
	conn.close()

	return render_template("lounge_room.html")

@app.route("/best_room")
def best_room():
	conn = sqlite3.connect("NFC-Data.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO NFC_Data VALUES(?,?)", (datetime.now().strftime("%H:%M"), "best room"))

	conn.commit()
	conn.close()

	return render_template("best_room.html")

@app.route("/dining_room")
def dining_room():
	conn = sqlite3.connect("NFC-Data.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO NFC_Data VALUES(?,?)", (datetime.now().strftime("%H:%M"), "dining room"))

	conn.commit()
	conn.close()

	return render_template("dining_room.html")

@app.route("/kitchen_room")
def kitchen_room():
	conn = sqlite3.connect("NFC-Data.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO NFC_Data VALUES(?,?)", (datetime.now().strftime("%H:%M"), "kitchen"))

	conn.commit()
	conn.close()

	return render_template("kitchen_room.html")

@app.route("/laundry")
def laundry_room():
	conn = sqlite3.connect("NFC-Data.db")
	cur = conn.cursor()

	cur.execute("INSERT INTO NFC_Data VALUES(?,?)", (datetime.now().strftime("%H:%M"), "laundry"))

	conn.commit()
	conn.close()

	return render_template("laundry_room.html")

app.run(debug=True)