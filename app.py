from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("all_states_forecast.csv")

@app.get("/")
def home():
    return {"message": "Sales Forecast API Running"}

@app.get("/forecast")
def get_all_forecast():
    return df.to_dict()

@app.get("/forecast/{state}")
def get_state_forecast(state: str):
    result = df[df['State'] == state]
    return result.to_dict()