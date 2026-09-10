import joblib
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app = FastAPI(title ="Api de prediccion de precios de viviendas",description="Api para predecir el precio de una vivienda en base a su superficie en metros cuadrados",version="1.0.0")

try:
    # cargar modelo entrenado
    model = joblib.load("./Models/linea_model.pkl")
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Modelo no encontrado. Asegúrese de que el modelo esté entrenado y guardado correctamente.")

# definicion de esquema de la entrada de la prediccion
class housem2(BaseModel):
    area_m2: float = Field(..., example=100.0, description="Superficie de la vivienda en metros cuadrados")

@app.get("/")
def health_check():
    return {"status": "OK", "message": "API de predicción de precios de viviendas está en funcionamiento.","model_loaded": model is not None}

@app.post("/predict")
def predict_price(data: housem2):
    if not model:
        raise HTTPException(status_code=500, detail="Modelo no cargado. Asegúrese de que el modelo esté entrenado y guardado correctamente.")
    # realizar prediccion
    prediction = model.predict([[data.area_m2]])[0]
    return{
        "area_m2": data.area_m2,
        "predicted_price": round(prediction,2)
    }
