import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/reviews.csv")

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

for _, row in df.iterrows():

    cur.execute("""
        INSERT INTO reviews (
            review_id,
            agent,
            review_date,
            tickets_reviewed,
            ovv_score,
            qa_score
        )
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        int(row.review_id),
        row.agent,
        row.date,
        int(row.tickets_reviewed),
        int(row.ovv_score),
        int(row.qa_score)
    ))

conn.commit()

print(f"Loaded {len(df)} records")

cur.close()
conn.close()
