import pandas as pd
import numpy as np
def calculate_ema20(df):
    df["EMA20"] = df["Close"].ewm(span=20, adjust=False).mean()
    return df
def calculate_ema50(df):
    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()
    return df
def calculate_rsi14(df):
    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    average_gain = gain.rolling(window=14).mean()
    average_loss = loss.rolling(window=14).mean()

    rs = average_gain / average_loss
    df["RSI14"] = 100 - (100 / (1 + rs))

    return df
def calculate_volume_ma20(df):
    df["Volume_MA20"] = df["Volume"].rolling(window=20).mean()
    return df
def generate_signal(df):
    df["Signal"] = "HOLD"

    buy_condition = (
    (df["EMA20"] > df["EMA50"]) &
    (df["EMA20"].shift(1) <= df["EMA50"].shift(1)) &
    (df["RSI14"] > 50) &
    (df["Volume"] > 1.5 * df["Volume_MA20"])
    )

    sell_condition = (
        (df["RSI14"] > 70) &
        (df["RSI14"] < df["RSI14"].shift(1))
    )

    df.loc[buy_condition, "Signal"] = "BUY"
    df.loc[sell_condition, "Signal"] = "SELL"

    return df
def run_strategy(df):
    df = calculate_ema20(df)
    df = calculate_ema50(df)
    df = calculate_rsi14(df)
    df = calculate_volume_ma20(df)
    df = generate_signal(df)

    return df
if __name__ == "__main__":
    print("Strategy file OK")