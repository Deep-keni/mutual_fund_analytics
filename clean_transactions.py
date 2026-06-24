from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parent
transactions_path = ROOT / "data" / "raw" / "08_investor_transactions.csv"

transactions_df = pd.read_csv(transactions_path)

transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'])

transactions_df['transaction_type'] = transactions_df['transaction_type'].str.upper()
transactions_df = transactions_df[transactions_df['transaction_type'].isin(['SIP','LUMPSUM','REDEMPTION'])]

transactions_df = transactions_df[transactions_df['amount_inr'] > 0]

print(transactions_df['kyc_status'].value_counts())
transactions_df['kyc_status'] = transactions_df['kyc_status'].str.upper().str.replace(' ', '_')

print(f"Number of duplicate rows: {transactions_df.duplicated().sum()}")

transactions_df.to_csv("data/processed/transactions_clean.csv", index=False)
print("✅ Saved: transactions_clean.csv")