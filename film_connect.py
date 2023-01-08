import sqlite3 as sql

conn = sql.connect(
    "C:/Users/cecil/OneDrive/Documents/Bootcamp/B10_Python_Week_2/Project_Filmflix/filmflix.db")
cursor = conn.cursor()

if conn:
    print("Database is connected")
else:
    print("Check error message, unable to connect")
