from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector


app = Flask(__name__)

app.config['SECRET_KEY'] = 'privatni-casovi-flask'

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='januar2022'
)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 