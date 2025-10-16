from flask import Flask, render_template
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',  
    'db': 'flaskdb',
    'port': 3306,
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def home():
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()   # list of tuples
    finally:
        cur.close()
        conn.close()
    return render_template('home.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)