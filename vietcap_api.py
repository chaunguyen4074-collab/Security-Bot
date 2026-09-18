import os
import requests
import pandas as pd
from dotenv import load_dotenv
from strategy import run_strategy
load_dotenv()


def get_stock_data(symbol):
    url = "https://trading.vietcap.com.vn/api/chart/OHLCChart/gap-chart"

    data = {
        "timeFrame": "ONE_DAY",
        "symbols": [symbol],
        "countBack": 1030,
        "to": 1753142400
    }

    response = requests.post(
        url,
        json=data,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        raise Exception("Không lấy được dữ liệu từ Vietcap API")

    print("Status code:", response.status_code)

    result = response.json()
    data = result[0]

    df = pd.DataFrame({
        "Date": pd.to_datetime(pd.Series(data["t"]).astype(int), unit="s"),
        "Open": data["o"],
        "High": data["h"],
        "Low": data["l"],
        "Close": data["c"],
        "Volume": data["v"]
    })
    df = run_strategy(df)
    return df

url = "https://trading.vietcap.com.vn/api/chart/OHLCChart/gap-chart"

token = os.getenv("VIETCAP_ACCESS_TOKEN")
device_id = os.getenv("VIETCAP_DEVICE_ID")

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "device-id": device_id,
    "origin": "https://trading.vietcap.com.vn",
    "referer": "https://trading.vietcap.com.vn/priceboard",
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"Bearer {token}"
}

