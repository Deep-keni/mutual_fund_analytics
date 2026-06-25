from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parent

# Create SQLite database
engine = create_engine(f"sqlite:///{ROOT}/bluestock_mf.db")

# Read schema.sql and execute it
with engine.connect() as conn:
    with open(ROOT / "sql" / "schema.sql", "r") as f:
        schema = f.read()
    for statement in schema.split(";"):
        if statement.strip():
            conn.execute(text(statement))
    conn.commit()
print("Schema created")

# Quick clean for fund_master
fm = pd.read_csv(ROOT / "data/raw/01_fund_master.csv")
fm.to_csv(ROOT / "data/processed/fund_master_clean.csv", index=False)

# Load cleaned CSVs into tables
tables = {
    "dim_fund" : "data/processed/fund_master_clean.csv",
    "fact_nav" : "data/processed/nav_history_clean.csv",
    "fact_transactions" : "data/processed/transactions_clean.csv",
    "fact_performance" : "data/processed/scheme_performance_clean.csv",
}

for table, path in tables.items():
    df = pd.read_csv(ROOT / path)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows → {table}")

print("\nDatabase ready: bluestock_mf.db")