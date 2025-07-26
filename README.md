# btc_long_forecast

📈 BTC Long-Term Insights: Predicción de Precio de Bitcoin hasta 2030 usando IA y Datos Multifuente

🧠 Proyecto personal | ⚙️ Python · ML · Datos Económicos · On‑Chain · Sentimiento

📌 Descripción
Este proyecto realiza una predicción del precio de Bitcoin hasta el año 2030, integrando múltiples fuentes de datos que influyen en el comportamiento de BTC a largo plazo. Se trata de un sistema simplificado que combina técnicas de Machine Learning con indicadores reales y teóricos relacionados con:

📊 Factores macroeconómicos
🔗 Datos on-chain
💬 Sentimiento de mercado
📚 Entorno regulatorio y adopción institucional
🚀 Avances tecnológicos y estructura de mercado

El objetivo es mostrar un enfoque integrador para prever tendencias más allá del análisis técnico básico, aplicando principios reales de Data Engineering y predicción con IA.

🧩 Estructura del proyecto
btc_long_forecast/
├── data_fetch.py          # Descarga datos históricos y simulados (BTC, macro, on-chain)
├── data_processing.py     # Limpieza, fusión y preparación de dataset completo
├── model_train.py         # Entrenamiento de modelo ML (SVR) y validación sobre histórico
├── forecast.py            # Predicción 2025–2030 usando variables extrapoladas
├── merged_features.csv    # Dataset principal resultante
├── btc_forecast_2030.csv  # Salida de predicción hasta 2030
├── historical_fit.png     # Gráfico histórico comparado con modelo
├── btc_forecast_2030.png  # Predicción gráfica 2025–2030
├── requirements.txt
└── README.md

⚙️ Tecnologías usadas
Python
pandas, numpy – manipulación y análisis de datos
yfinance – descarga de datos históricos de BTC
scikit-learn – regresión SVR
matplotlib – visualización
joblib – almacenamiento del modelo entrenado

📥 Datos utilizados (simplificados para MVP)
Histórico de BTC/USD (2015–2025)
Fuente: Yahoo Finance vía yfinance.
Indicadores macroeconómicos (dummy)
Tasa de interés de EE. UU.
Inflación anual
Indicadores on-chain (dummy)
Direcciones activas
Volumen movido por “whales”

Nota: los datos macro y on-chain se han simulado en esta versión inicial por no disponer de APIs públicas gratuitas fiables. En una versión avanzada se integrarían fuentes como Glassnode, FRED, [Google Trends API], [Alternative.me] y [CoinMetrics].

🧪 Cómo ejecutar
1. Clona el repositorio
bash
Copiar
Editar
git clone https://github.com/tuusuario/btc_long_forecast.git
cd btc_long_forecast

2. Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt

3. Descarga y prepara los datos
bash
Copiar
Editar
python data_fetch.py
python data_processing.py

4. Entrena el modelo
bash
Copiar
Editar
python model_train.py

5. Genera la predicción a largo plazo (2025–2030)
bash
Copiar
Editar
python forecast.py

📊 Resultados
🟠 Ajuste histórico del modelo SVR
<img src="historical_fit.png" alt="Fit histórico" width="700"/>
🟡 Predicción BTC 2025–2030
<img src="btc_forecast_2030.png" alt="Predicción BTC hasta 2030" width="700"/>
📄 Salida CSV
btc_forecast_2030.csv:
+------------+--------------+
|   Fecha    | Predicción $ |
+------------+--------------+
| 2025-01-01 |  58,935.00   |
| 2026-01-01 |  62,200.34   |
| 2027-01-01 |  65,910.12   |
| 2028-01-01 |  69,843.77   |
| 2029-01-01 |  73,900.23   |
| 2030-01-01 |  78,023.00   |
+------------+--------------+

🎯 Aprendizajes y posibles mejoras
Este proyecto representa un modelo inicial de predicción integradora multivariable, orientado a análisis de inversión a largo plazo. Algunas mejoras futuras serían:
Reemplazar datos dummy por datos reales vía API (Glassnode, FRED, Alternative.me).
Usar modelos más potentes: LSTM, ARIMA, Prophet o Transformer.
Incorporar NLP para detectar sentimiento desde redes sociales y prensa.
Automatizar ingesta y retraining en notebooks reproducibles.

🤝 Sobre mí
Samu, estudiante de CFGS en Desarrollo de Aplicaciones Multiplataforma (DAM) con enfoque en IA y ciencia de datos.

Este proyecto ha sido desarrollado como muestra de mis capacidades para integrar fuentes complejas de datos, preprocesar, modelar y generar insights accionables, y está orientado a candidaturas de prácticas en empresas.
