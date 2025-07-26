# data_fetch.py
# Descarga datos históricos y simulados (BTC, macro, on-chain)

import yfinance as yf
import pandas as pd
import requests

def fetch_btc_history():
    df = yf.download('BTC-USD', start='2015-01-01')
    df = df[['Close', 'Volume']].dropna()
    df.to_csv('btc_history.csv')
    return df

def fetch_macro_us():
    # ejemplo: data dummy, en real conectar API o usar CSV económico
    df = pd.DataFrame({
        'date': pd.date_range('2015-01-01', periods=len(range(2015,2025)), freq='Y'),
        'interest_rate': [0.5 + x*0.1 for x in range(len(range(2015,2025)))],
        'inflation_rate': [2 + x*0.2 for x in range(len(range(2015,2025)))]
    })
    df.to_csv('macro_us.csv', index=False)
    return df

def fetch_onchain_dummy():
    df = pd.DataFrame({
        'date': pd.date_range('2015-01-01', periods=len(range(2015,2025)), freq='Y'),
        'active_addresses': [100000 + x*5000 for x in range(len(range(2015,2025)))],
        'whale_volume': [500 + x*50 for x in range(len(range(2015,2025)))]
    })
    df.to_csv('onchain.csv', index=False)
    return df

if __name__ == "__main__":
    fetch_btc_history()
    fetch_macro_us()
    fetch_onchain_dummy()
