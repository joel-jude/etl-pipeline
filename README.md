# QA Pipeline Demo

Demo ETL pipeline showing:

1. Generate review data
2. Store review data in CSV
3. Load CSV into PostgreSQL
4. Query review records for QA analysis

## Setup

```bash
pip install -r requirements.txt
```

Copy:

```bash
cp .env.example .env
```

Update database credentials.

## Run

Generate sample data:

```bash
python scripts/generate_reviews.py
```

Create table:

```bash
python scripts/create_table.py
```

Load data:

```bash
python scripts/load_reviews.py
```

## Schema

| Column | Description |
|----------|----------|
| review_id | Review identifier |
| agent | Agent reviewed |
| review_date | Review date |
| tickets_reviewed | Tickets reviewed |
| ovv_score | Original review score |
| qa_score | QA challenge score |
