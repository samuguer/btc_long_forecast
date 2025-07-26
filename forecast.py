# forecast.py
# Predicción 2025–2030 usando variables extrapoladas

import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

model, scaler = joblib.load('svr_model.pkl')
df = pd.read_csv('merged_features.csv', parse_dates=['date'])

# Crear dataset futuro (2025–2030) con valores extrapolados
future = pd.DataFrame({
    'date': pd.date_range('2025-01-01','2030-01-01', freq='AS'),
    'interest_rate': np.linspace(df['interest_rate'].iloc[-1], df['interest_rate'].iloc[-1]+2, 6),
    'inflation_rate': np.linspace(df['inflation_rate'].iloc[-1], df['inflation_rate'].iloc[-1]+1, 6),
    'active_addresses': np.linspace(df['active_addresses'].iloc[-1], df['active_addresses'].iloc[-1]*1.5, 6),
    'whale_volume': np.linspace(df['whale_volume'].iloc[-1], df['whale_volume'].iloc[-1]*1.5, 6),
    'Volume': np.linspace(df['Volume'].iloc[-1], df['Volume'].iloc[-1]*1.2, 6),
})
Xf = scaler.transform(future[['interest_rate','inflation_rate','active_addresses','whale_volume','Volume']])
future['pred_close'] = model.predict(Xf)

# Visualización
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['Close'], label='Real')
plt.plot(future['date'], future['pred_close'], label='Predicción 2025‑2030', linestyle='--')
plt.legend()
plt.title('Predicción BTC hasta 2030')
plt.savefig('btc_forecast_2030.png')
plt.show()

future.to_csv('btc_forecast_2030.csv', index=False)
print(future)
