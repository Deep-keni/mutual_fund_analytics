1. Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

2. Average NAV per month for each fund
SELECT amfi_code,
strftime('%Y-%m', date) AS month,
ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

3. SIP inflow YoY growth
SELECT strftime('%Y', transaction_date) AS year,
ROUND(SUM(amount_inr), 2) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

4. Transactions count by state
SELECT state,
COUNT(*) AS total_transactions,
ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

5. Funds with expense_ratio < 1%
SELECT f.scheme_name, f.fund_house, f.expense_ratio_pct
FROM dim_fund f
WHERE f.expense_ratio_pct < 1.0
ORDER BY f.expense_ratio_pct ASC;

6. Best performing funds by 3Y returns
SELECT f.scheme_name, p.return_3yr_pct, p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 10;

7. Transaction volume by type
SELECT transaction_type,
COUNT(*) AS count,
ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

8. Funds with highest Sharpe ratio
SELECT f.scheme_name, f.category, p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;

9. NAV trend for SBI Bluechip (last 30 days)
SELECT date, nav
FROM fact_nav
WHERE amfi_code = '119551'
ORDER BY date DESC
LIMIT 30;

10. Gender-wise SIP investment split
SELECT gender,
COUNT(*) AS count,
ROUND(SUM(amount_inr), 2) AS total_invested
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY gender
ORDER BY total_invested DESC;