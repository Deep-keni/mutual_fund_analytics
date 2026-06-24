import requests
import pandas as pd

# All 5 schemes with their AMFI codes
schemes = {
    "sbi_bluechip" : 119551,
    "icici_bluechip" : 120503,
    "nippon_largecap" : 118632,
    "axis_bluechip" : 119092,
    "kotak_bluechip" : 120841
}

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nav_records = data["data"]
        df = pd.DataFrame(nav_records)
        df.to_csv(f"data/raw/{scheme_name}_nav.csv", index=False)
        print(f"Saved: {scheme_name}_nav.csv — {len(df)} rows")
    else:
        print(f"Failed: {scheme_name} — Status: {response.status_code}")

# Fetched live data from "https://api.mfapi.in/mf/125497" and saved it to "data/raw/sbi_bluechip_nav.csv" , then later just edited the code to find more live data from given 5 schemes and saved them to their respective CSV files.