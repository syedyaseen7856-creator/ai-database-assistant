import sqlite3
import os

DB_PATH = r"C:\Users\DELL\OneDrive\Desktop\AI Database Assistant\backend\company.db"

print("USING DB FILE:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# FORCE RESET
cursor.execute("DROP TABLE IF EXISTS employees")

# CREATE TABLE
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
""")

# INSERT DATA
cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("John", "IT", 60000),
    ("Alice", "HR", 55000),
    ("Bob", "Finance", 70000)
])

conn.commit()

# VERIFY INSIDE SCRIPT (IMPORTANT)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("TABLES CREATED:", cursor.fetchall())

cursor.execute("SELECT * FROM employees")
print("DATA:", cursor.fetchall())

conn.close()

print("✅ DATABASE FULLY CREATED")