import sqlite3

#DB Conection
conn = sqlite3.connect('kiosk.db')
cursor = conn.cursor()

#DB Initial Table Query
sql_query = """CREATE TABLE IF NOT EXISTS
interaction(int_id INTEGER PRIMARY KEY, iniTime DATETIME, endTime DATETIME, decisionOne STRING, decisionTwo STRING, language STRING)"""
cursor.execute(sql_query)