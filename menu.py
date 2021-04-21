from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_bootstrap import Bootstrap

import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def greetings():
    return ("Hello Customers! \n We are reimagining our menu and would like your help! \n Instructions: \n Type /menu to see the categories of food being added. \n From there type click on whichever category you would like to vote on! \n After you've voted, you can /menu/'category'/results to see what others have suggested. \n We appreciate it!")

@app.route("/menu")
def menu_items():
    return render_template("menucategories.html")

@app.route("/menu/pizza")
def pizza():
    return render_template("pizza.html")

@app.route("/menu/pizza/results")
def list_dataP():
    con = sql.connect("pizzadatabase.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM pizza")

    rows = cur.fetchall()
    return render_template("pizzalist.html", rows = rows)

@app.route("/resultsP", methods={"POST"})
def resultsP():
    if request.method == "POST":
        name = request.form["nm"]
        chone = request.form["one"]
        chtwo = request.form["two"]

        with sql.connect("pizzadatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO pizza (name, Choice1, Choice2) VALUES (?, ?, ?)", [name, chone, chtwo])
        con.commit()

        return "Record successfully added {0} {1} {2}, Thank you!" .format(name, chone, chtwo)

# def create_databaseP():
#     conn = sql.connect("pizzadatabase.db")
#     conn.execute("CREATE TABLE pizza (name TEXT, choice1 TEXT, choice2 TEXT)")
#     conn.close()

# create_databaseP()

@app.route("/menu/subs")
def subs():
    return render_template("subs.html")

@app.route("/menu/subs/results")
def list_dataS():
    con = sql.connect("subsdatabase.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM subs")

    rows = cur.fetchall()
    return render_template("subslist.html", rows = rows)

@app.route("/resultsS", methods={"POST"})
def resultsS():
    if request.method == "POST":
        name = request.form["nm"]
        chone = request.form["one"]
        chtwo = request.form["two"]

        with sql.connect("subsdatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO subs (name, Choice1, Choice2) VALUES (?, ?, ?)", [name, chone, chtwo])
        con.commit()

        return "Record successfully added {0} {1} {2}, Thank you!" .format(name, chone, chtwo)

# def create_databaseS():
#     conn = sql.connect("subsdatabase.db")
#     conn.execute("CREATE TABLE subs (name TEXT, choice1 TEXT, choice2 TEXT)")
#     conn.close()

# create_databaseS()

@app.route("/menu/apps")
def apps():
    return render_template("apps.html")

@app.route("/menu/apps/results")
def list_dataA():
    con = sql.connect("appsdatabase.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM apps")

    rows = cur.fetchall()
    return render_template("appslist.html", rows = rows)

@app.route("/resultsA", methods={"POST"})
def resultsA():
    if request.method == "POST":
        name = request.form["nm"]
        chone = request.form["one"]
        chtwo = request.form["two"]

        with sql.connect("appsdatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO apps (name, Choice1, Choice2) VALUES (?, ?, ?)", [name, chone, chtwo])
        con.commit()

        return "Record successfully added {0} {1} {2}, Thank you!" .format(name, chone, chtwo)

# def create_databaseA():
#     conn = sql.connect("appsdatabase.db")
#     conn.execute("CREATE TABLE apps (name TEXT, choice1 TEXT, choice2 TEXT)")
#     conn.close()

# create_databaseA()

@app.route("/menu/drinks")
def drinks():
    return render_template("drinks.html")

@app.route("/menu/drinks/results")
def list_dataD():
    con = sql.connect("drinksdatabase.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM drinks")

    rows = cur.fetchall()
    return render_template("drinkslist.html", rows = rows)

@app.route("/resultsD", methods={"POST"})
def resultsD():
    if request.method == "POST":
        name = request.form["nm"]
        chone = request.form["one"]
        chtwo = request.form["two"]

        with sql.connect("drinksdatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO drinks (name, Choice1, Choice2) VALUES (?, ?, ?)", [name, chone, chtwo])
        con.commit()

        return "Record successfully added {0} {1} {2}, Thank you!" .format(name, chone, chtwo)

# def create_databaseD():
#     conn = sql.connect("drinksdatabase.db")
#     conn.execute("CREATE TABLE drinks (name TEXT, choice1 TEXT, choice2 TEXT)")
#     conn.close()

# create_databaseD()


if __name__ == '__main__':
    app.run(debug=True)