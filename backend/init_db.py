import sqlite3

# Create or connect database file
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('John', 'IT', 60000)")
cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Alice', 'HR', 55000)")
cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Bob', 'Finance', 70000)")

conn.commit()
conn.close()

print("✅ Database initialized successfully!")