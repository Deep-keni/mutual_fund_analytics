# Data Dictionary — Bluestock MF Analytics Platform

## dim_fund
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| amfi_code | TEXT | Unique AMFI scheme code — primary key | 01_fund_master.csv |
| fund_house | TEXT | AMC name (SBI, HDFC, ICICI etc.) | 01_fund_master.csv |
| scheme_name | TEXT | Full name of the mutual fund scheme | 01_fund_master.csv |
| category | TEXT | Broad category — Equity / Debt / Hybrid | 01_fund_master.csv |
| sub_category | TEXT | SEBI sub-category — Large Cap, Mid Cap etc. | 01_fund_master.csv |
| expense_ratio_pct | REAL | Annual fee charged to investors (0.1–2.5%) | 01_fund_master.csv |
| risk_category | TEXT | Risk grade — Low / Moderate / High | 01_fund_master.csv |
| fund_manager | TEXT | Name of the fund manager | 01_fund_master.csv |

## dim_date
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| date | DATE | Primary key — calendar date | Generated |
| year | INTEGER | Calendar year | Generated |
| quarter | INTEGER | Quarter (1–4) | Generated |
| month | INTEGER | Month number (1–12) | Generated |
| day | INTEGER | Day of month | Generated |

## fact_nav
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| amfi_code | TEXT | FK → dim_fund | 02_nav_history.csv |
| date | DATE | FK → dim_date | 02_nav_history.csv |
| nav | REAL | Net Asset Value — price of 1 unit of fund | 02_nav_history.csv |

## fact_transactions
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| transaction_id | INTEGER | Unique transaction identifier | 08_investor_transactions.csv |
| amfi_code | TEXT | FK → dim_fund | 08_investor_transactions.csv |
| transaction_date | DATE | FK → dim_date | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP / LUMPSUM / REDEMPTION | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction amount in INR | 08_investor_transactions.csv |
| state | TEXT | Investor's state | 08_investor_transactions.csv |
| city_tier | TEXT | Tier 1 / Tier 2 / Tier 3 city | 08_investor_transactions.csv |
| kyc_status | TEXT | KYC_VERIFIED / KYC_PENDING / KYC_REJECTED | 08_investor_transactions.csv |

## fact_performance
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| amfi_code | TEXT | FK → dim_fund | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1 year return percentage | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3 year return percentage | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5 year return percentage | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Risk-adjusted return metric | 07_scheme_performance.csv |
| sortino_ratio | REAL | Downside risk-adjusted return | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Largest peak-to-trough decline | 07_scheme_performance.csv |
| alpha | REAL | Excess return vs benchmark | 07_scheme_performance.csv |
| beta | REAL | Sensitivity to market movement | 07_scheme_performance.csv |

## fact_aum
| Column | Type | Description | Source |
|--------|------|-------------|--------|
| fund_house | TEXT | AMC name | 03_aum_by_fund_house.csv |
| date | DATE | FK → dim_date | 03_aum_by_fund_house.csv |
| aum_crore | REAL | Assets Under Management in crores | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of active schemes | 03_aum_by_fund_house.csv |