import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

import os

def get_db():
    db_path = os.path.join(os.path.dirname(__file__), 'spots.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    city = request.args.get('city', '')
    companion = request.args.get('companion', '')
    genre = request.args.get('genre', '')
    duration = request.args.get('duration', '')

    query = 'SELECT * FROM spots WHERE 1=1'
    params = []

    if city:
        query += ' AND city = ?'
        params.append(city)
    if companion:
        query += ' AND companion = ?'
        params.append(companion)
    if genre:
        query += ' AND genre = ?'
        params.append(genre)
    if duration:
        query += ' AND duration = ?'
        params.append(duration)

    conn = get_db()
    spots = conn.execute(query, params).fetchall()
    conn.close()

    return render_template('results.html', spots=spots)

@app.route('/spot/<int:id>')
def detail(id):
    conn = get_db()
    spot = conn.execute('SELECT * FROM spots WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('detail.html', spot=spot)

if __name__ == '__main__':
    app.run(debug=True)