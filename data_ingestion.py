import pandas as pd
import os

# ============================================================
# 1 . Basic View of all datasets in data/raw folder
# ============================================================

print("\n" + "="*50)
print("BASIC VIEW OF ALL DATASETS")
print("="*50)

# dictionary of all datasets to load and view basic info
datasets = {
    "fund_master" : "data/raw/01_fund_master.csv",
    "nav_history" : "data/raw/02_nav_history.csv",
    "aum_by_fund_house" : "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows" : "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows" : "data/raw/05_category_inflows.csv",
    "industry_folio_count" : "data/raw/06_industry_folio_count.csv",
    "scheme_performance" : "data/raw/07_scheme_performance.csv",
    "investor_transactions" : "data/raw/08_investor_transactions.csv",
    "portfolio_holdings" : "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices" : "data/raw/10_benchmark_indices.csv",
}

for name, path in datasets.items():
    print(f"\n{'='*50}")
    print(f"Dataset: {name}")
    print(f"{'='*50}")

    df = pd.read_csv(path)

    print(f"Shape : {df.shape}")
    print(f"Columns : {list(df.columns)}")
    print(f"\nData Types : \n{df.dtypes}")
    print(f"\nMissing Values : \n{df.isnull().sum()}")
    print(f"\nFirst 3 rows : \n{df.head(3)}")


# ============================================================
# 2 . Exploring fund_master dataset
# ============================================================

print("\n" + "="*50)
print("FUND MASTER EXPLORATION")
print("="*50)

fm = pd.read_csv("data/raw/01_fund_master.csv")

print(f"\nUnique Fund Houses : {fm['fund_house'].nunique()}")
print(fm['fund_house'].unique())
print(f"\nUnique Categories : {fm['category'].nunique()}")
print(fm['category'].unique())
print(f"\nUnique Sub-Categories : {fm['sub_category'].nunique()}")
print(fm['sub_category'].unique())
print(f"\nRisk Grade Distribution:")
print(fm['risk_category'].value_counts())


# ============================================================
# 3 . AMFI Code Validation
# ============================================================

print("\n" + "="*50)
print("AMFI CODE VALIDATION")
print("="*50)

nh = pd.read_csv("data/raw/02_nav_history.csv")

fm_codes = set(fm['amfi_code'])
nh_codes = set(nh['amfi_code'])

missing = fm_codes - nh_codes

print(f"\nTotal codes in fund_master : {len(fm_codes)}")
print(f"Total codes in nav_history : {len(nh_codes)}")
print(f"Codes missing in nav_history : {len(missing)}")

if len(missing) == 0:
    print("All AMFI codes validated — no mismatches found")
else:
    print(f"Missing codes: {missing}")