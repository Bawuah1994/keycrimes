import sqlite3 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('keycrime_data.db')

    # The function below is to display the department id without linking it to the department data table
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from keycrime")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")