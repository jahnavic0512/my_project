import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def get_products():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Admin@123', 
        database='my_budget_db'
    )
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT day, budget, status FROM weekly_budget")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route('/')
def home():
    return render_template('index.html', weekdays=get_products())

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, port=7000)