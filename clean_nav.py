from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parent
nav_history_path = ROOT / "data" / "raw" / "02_nav_history.csv"

nav_hist_df = pd.read_csv(nav_history_path)

nav_hist_df['date'] = pd.to_datetime(nav_hist_df['date'])

nav_hist_df = nav_hist_df.sort_values(by=['amfi_code','date'])

print(nav_hist_df.isnull().sum())
# Since there are 0 null values in all the 3 cols , we need not do forward filling process .

print(nav_hist_df.duplicated().sum())
# Also 0 duplicates are there , so we can also skip this step .

# Filtering the Nav values <= 0 
nav_hist_df = nav_hist_df[nav_hist_df['nav'] > 0]

nav_hist_df.to_csv("data/processed/nav_history_clean.csv", index=False)
print("✅ Saved: nav_history_clean.csv")