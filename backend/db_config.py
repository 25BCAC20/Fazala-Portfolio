import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-B3EH7K6\SQLEXPRESS;'  # Replace with your instance
        r'DATABASE=portfolio_db;'
        r'UID=sa;'  # Your SQL Server username
        r'PWD=adminadmin'  # Your SQL Server password
    )
    return conn
