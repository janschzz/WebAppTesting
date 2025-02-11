import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Read database configuration from environment variables
DB_HOST = os.getenv("DB_HOST", "database-1.c38m6e8g2070.eu-north-1.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "test")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "xynzyc-cyhdi3-xIpcyv")
DB_PORT = os.getenv("DB_PORT", "5432")

@app.route("/")
def index():
    try:
        # Establish a connection to the Postgres database
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        # Change the query to match a table that exists in your database.
        # For example, if you have a table named "my_table":
        cur.execute("SELECT * FROM users LIMIT 5;")
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        # Return the data as JSON
        return jsonify(rows)
    except Exception as e:
        # Return the error message and a 500 status code if something goes wrong
        return f"Error connecting to the DB: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
