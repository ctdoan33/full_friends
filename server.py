from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends_db')
@app.route("/")
def index():
    query = "SELECT name, age, DATE_FORMAT(created_at, '%b %D %Y') AS friend_since FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route("/insert", methods=["POST"])
def insert():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
        "name" : request.form["name"],
        "age" : request.form["age"]
    }
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)
