import sqlite3
connection = sqlite3.connect('finance.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS weekly_budget')
cursor.execute('''
    CREATE TABLE weekly_budget (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT NOT NULL,
        budget TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

initial_data = [
    ("Monday", "₹1,500", "Workday"),
    ("Tuesday", "₹1,200", "Workday"),
    ("Wednesday", "₹1,200", "Workday"),
    ("Thursday", "₹1,500", "Workday"),
    ("Friday", "₹2,000", "Workday"),
    ("Saturday", "₹3,500", "Weekend"),
    ("Sunday", "₹4,000", "Weekend")
]

cursor.executemany(
    'INSERT INTO weekly_budget (day, budget, status) VALUES (?, ?, ?)', 
    initial_data
)

connection.commit()
connection.close()

print("Database 'finance.db' created and populated successfully!")