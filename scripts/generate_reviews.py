import random
from datetime import datetime, timedelta
import pandas as pd

NUM_REVIEWS = 100

agents = [
    "Alice",
    "Bob",
    "Carlos",
    "Diana",
    "Emma",
    "Frank"
]

rows = []

for review_id in range(1000, 1000 + NUM_REVIEWS):

    ovv_score = random.randint(70, 100)

    if random.random() < 0.35:
        qa_score = min(100, ovv_score + random.randint(1, 10))
    else:
        qa_score = max(0, ovv_score + random.randint(-3, 3))

    rows.append({
        "review_id": review_id,
        "agent": random.choice(agents),
        "date": (
            datetime(2025, 1, 1)
            + timedelta(days=random.randint(0, 180))
        ).strftime("%Y-%m-%d"),
        "tickets_reviewed": random.randint(5, 40),
        "ovv_score": ovv_score,
        "qa_score": qa_score
    })

df = pd.DataFrame(rows)

df.to_csv("data/reviews.csv", index=False)

print("Created data/reviews.csv")
