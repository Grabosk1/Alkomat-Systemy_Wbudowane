from flask import Flask, request, render_template, jsonify, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import nltk
from autocorrect import spell
from gensim.summarization import summarize as g_sumn

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/raport', methods=["GET", "POST"])
def raport():
    if request.method == 'GET':
        db_r, cursor_r = cursor()

        cursor_r.execute('SELECT * FROM wyniki')
        all_rows = cursor_r.fetchall()
        return render_template('raport.html', items=all_rows)
    else:
        db_r, cursor_r = cursor()

        print('test')

        cursor_r.execute('DELETE FROM wyniki WHERE id > 0')

        db_r.commit()

        return render_template('raport.html')


@app.route('/projekt', methods=["GET"])
def projekt():
    return render_template('projekt.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login')
        haslo = request.form.get('hasło')

        if login == 'admin' and haslo == "admin":
            return render_template('modyfikacje.html')
        else:
            flash("Błędne dane logowania! Proszę sprawdzić dane logowania i spróbować ponownie.")
            return render_template('login.html')


def cursor():
    db = sqlite3.connect('Baza_Danych.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS wyniki(id INTEGER PRIMARY KEY, pomiar REAL, karta VARCHAR , text VARCHAR);')
    db.commit()

    # pomiar = 123
    # prac = 'Kurier'
    # decyzja = 'Zdolny do pracy'

    # cursor.execute('INSERT INTO wyniki(pomiar, karta, text) '
    #               'VALUES(?,?,?)', (pomiar, str(prac), str(decyzja)))
    # db.commit()

    return db, cursor


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1234)
