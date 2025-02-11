import os
import psycopg2
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Pull credentials/config from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "secret")
DB_PORT = int(os.getenv("DB_PORT", "5432"))

@app.route("/")
def index():
    try:
        # Connect to the Postgres database
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cur = conn.cursor()
        # Example: query a table named "my_table"
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        
        cur.close()
        conn.close()

        # Return results in a simple JSON for now (or use render_template for HTML)
        return jsonify(rows)
    except Exception as e:
        return f"Error connecting to the DB: {str(e)}"

if __name__ == "__main__":
    # For local dev only. In production, you'll run Gunicorn instead.
    app.run(host="0.0.0.0", port=5000)

