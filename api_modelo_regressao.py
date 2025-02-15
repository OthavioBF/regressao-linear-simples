from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

app = FastAPI()

class RequestBody(BaseModel):
  horas_estudo: float
  
modelo_pontuacao = joblib.load('./modelo_regressao.pkl')

@app.post('/predict')
def predict(data: RequestBody):
  input_feature = [[data.horas_estudo]]
  
  y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
  
  return {'pontuacao_teste': y_pred.tolist()}
  
  