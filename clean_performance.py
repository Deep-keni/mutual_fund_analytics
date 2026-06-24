from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
performance_path = ROOT / "data" / "raw" / "07_scheme_performance.csv"

performance_df = pd.read_csv(performance_path)

# already numeric, no conversion needed
print(performance_df[['return_1yr_pct','return_3yr_pct','return_5yr_pct']].dtypes)

# Step C — flag return anomalies (outside -50% to +100%)
performance_df['is_anomaly'] = (
    (performance_df['return_1yr_pct'] < -50) | (performance_df['return_1yr_pct'] > 100) |
    (performance_df['return_3yr_pct'] < -50) | (performance_df['return_3yr_pct'] > 100) |
    (performance_df['return_5yr_pct'] < -50) | (performance_df['return_5yr_pct'] > 100)
)
print(f"Anomalous return rows: {performance_df['is_anomaly'].sum()}")

performance_df['expense_ratio_anomaly'] = ~performance_df['expense_ratio_pct'].between(0.1, 2.5)
print(f"Expense ratio anomalies: {performance_df['expense_ratio_anomaly'].sum()}")

performance_df.to_csv("data/processed/scheme_performance_clean.csv", index=False)
print("✅ Saved: scheme_performance_clean.csv")