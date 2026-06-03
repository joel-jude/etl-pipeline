import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    agent VARCHAR(50),
    review_date DATE,
    tickets_reviewed INTEGER,
    ovv_score INTEGER,
    qa_score INTEGER
);
""")

conn.commit()

print("Created reviews table")

cur.close()
conn.close()
