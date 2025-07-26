# model_train.py
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('merged_features.csv', parse_dates=['date'])
X = df[['interest_rate','inflation_rate','active_addresses','whale_volume','Volume']]
y = df['Close']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = SVR(kernel='rbf', C=1e3, gamma=0.1)
model.fit(X_scaled, y)

# curva de prueba histórica
pred = model.predict(X_scaled)
plt.plot(df['date'], y, label='Real')
plt.plot(df['date'], pred, label='Predicción (histórica)')
plt.legend()
plt.title('SVR BTC Price Fit Histórico')
plt.savefig('historical_fit.png')
plt.show()

import joblib
joblib.dump((model, scaler), 'svr_model.pkl')
