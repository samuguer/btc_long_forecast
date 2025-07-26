# data_processing.py
import pandas as pd

def merge_datasets():
    btc = pd.read_csv('btc_history.csv', parse_dates=['Date'])
    btc = btc.rename(columns={'Date': 'date'})
    macro = pd.read_csv('macro_us.csv', parse_dates=['date'])
    onchain = pd.read_csv('onchain.csv', parse_dates=['date'])
    df = pd.merge_asof(btc.sort_values('date'), macro.sort_values('date'), on='date')
    df = pd.merge_asof(df, onchain.sort_values('date'), on='date')
    df = df.fillna(method='ffill').dropna()
    return df

if __name__ == "__main__":
    df = merge_datasets()
    print(df.head())
    df.to_csv('merged_features.csv', index=False)
