# ✈️ Flight Delay Predictor – Machine Learning Pipeline + Deployment

Este proyecto utiliza machine learning para predecir el retraso en minutos de vuelos comerciales, usando un conjunto de datos real de más de 5 millones de registros. Incluye un pipeline completo de preprocesamiento, entrenamiento del modelo con XGBoost, y despliegue en la nube con una API REST creada con FastAPI.

---

## 🔍 Objetivo

Desarrollar un modelo de regresión capaz de predecir los minutos de retraso de llegada de un vuelo, utilizando información previa como hora de salida, aerolíneas, aeropuertos, y datos históricos de retrasos.

---

## 🧰 Tecnologías y herramientas utilizadas

- **Lenguaje:** Python 3
- **Librerías ML:** XGBoost, Scikit-learn, Pandas
- **API:** FastAPI
- **Despliegue:** AWS EC2 (capa gratuita), Uvicorn
- **Otras:** Label Encoding, DMatrix, EDA

---

## 🧠 Pasos del proyecto

1. **Análisis exploratorio de datos**
   - Dataset: vuelos comerciales en EE.UU. del año 2015 (https://www.kaggle.com/datasets/usdot/flight-delays?select=flights.csv)
   - Más de 5 millones de registros, en 31 columnas

2. **Preprocesamiento**
   - Eliminación de columnas que no eran relevantes o que contenian informacion redundante
   - Codificación de variables categóricas con Label Encoding
   - Imputacion de valores faltantes

3. **Entrenamiento del modelo**
   - Modelo: `XGBoostRegressor` (con `DMatrix` para eficiencia)
   - Métricas: RMSE, MAE
   - Optimizaciones: `subsample`, `colsample_bytree`, `max_depth`, `tree_method=hist`

4. **Despliegue en la nube**
   - Servidor EC2 gratuito (t2.micro)
   - API REST en FastAPI
   - Endpoint `/predict` para recibir datos y devolver predicción de retraso



## 🚀 Cómo probar la API

Se puede probar el modelo enviando un `POST` a:

```bash
http://34.201.50.77:8000/predict
```

Ejemplo con requests en Python:

```python
import requests

#url = "http://127.0.0.1:8000/predict"      # Local
url = "http://34.201.50.77:8000/predict"    # Deploy Nube

data = {
    "YEAR": 2024,
    "MONTH": 4,
    "DAY": 20,
    "DAY_OF_WEEK": 6,
    "AIRLINE": 3,
    "ORIGIN_AIRPORT": 10,
    "DESTINATION_AIRPORT": 45,
    "SCHEDULED_DEPARTURE": 830,
    "DEPARTURE_TIME": 845,
    "DEPARTURE_DELAY": 15.0,
    "TAXI_OUT": 10.0,
    "WHEELS_OFF": 855,
    "SCHEDULED_TIME": 120.0,
    "ELAPSED_TIME": 115.0,
    "AIR_TIME": 100.0,
    "DISTANCE": 1500.0,
    "WHEELS_ON": 955,
    "TAXI_IN": 5.0,
    "SCHEDULED_ARRIVAL": 950,
    "ARRIVAL_TIME": 960,
    "DIVERTED": 0,
    "AIR_SYSTEM_DELAY": 5.0,
    "SECURITY_DELAY": 0.0,
    "AIRLINE_DELAY": 10.0,
    "LATE_AIRCRAFT_DELAY": 0.0,
    "WEATHER_DELAY": 0.0
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Predicción:", response.json())
```

### 🏠 Ejecución Local

Si prefieres ejecutar la API localmente, simplemente instala las dependencias y ejecuta el servidor FastAPI en tu máquina:

1. Clona el repositorio:
```bash
git clone  https://github.com/j4carlos/delay_predict_API.git
cd delay_predict_API
```

2. Instala las dependencias
```bash
pip install -r requirements.txt
```
 3. Ejecuta FastAPI
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

La API estara disponible en htttp://127.0.0.1:8000/predict

## 📊 Resultados del Modelo

- **RMSE:** 2.73 minutos
- **MAE:** 0.96 minutos
- **Feature mas importante** Departure Delay

## Mejoras futuras:
- Contrastar resultados contra algun otro modelo, 
- revisar resultados con mas parametros
- agregar una funcion para que permita la carga de datos categoricos en formato no codificado cuando se realice una solicitud.

