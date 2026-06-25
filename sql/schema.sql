CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT NOT NULL,
    scheme_name TEXT NOT NULL,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);

CREATE TABLE fact_nav (
    amfi_code TEXT NOT NULL,
    date DATE NOT NULL,
    nav REAL NOT NULL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type TEXT NOT NULL,
    amount_inr REAL NOT NULL,
    investor_id TEXT,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (transaction_date) REFERENCES dim_date(date)
);

CREATE TABLE fact_performance (
    amfi_code TEXT PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    fund_house TEXT NOT NULL,
    date DATE NOT NULL,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER,
    PRIMARY KEY (fund_house, date),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);