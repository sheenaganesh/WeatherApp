from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import  requests

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api_key = "4ea1dd5d939e17386f697c3ded86afb7"



cities = {
    "London" : {"lat": 51.5072, "lon": -0.1276},
    "New York" : {"lat": 40.7128, "lon": -74.0060},
    "Paris" : {"lat": 48.8566, "lon": 2.3522}
}


@app.get("/{location}")
def read_root(location: str):
    coordinates = cities.get(location)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates.get("lat")}&lon={coordinates.get("lon")}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data.get("weather")[0].get("main")
        temperature = data.get("main").get("temp")
        return {"Weather": weather, "Temperature": temperature}
    else: 
        return {"error": "City not found"}
    