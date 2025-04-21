from fastapi import FastAPI, Request, HTTPException
import xgboost as xgb
import pandas as pd

# Cargar modelo previamente entrenado con xgb.train
model = xgb.Booster()
model.load_model("modelo_retrasos.model")

app = FastAPI(title="API de Predicción de Retrasos de Vuelos")

@app.get("/")
def root():
    return {"message": "Modelo de predicción de retrasos en vuelos"}

@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()
        df = pd.DataFrame([data])
        dmatrix = xgb.DMatrix(df)
        prediction = model.predict(dmatrix)
        return {"prediccion_retraso_minutos": round(float(prediction[0]),ndigits=4)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en la predicción: {str(e)}")
