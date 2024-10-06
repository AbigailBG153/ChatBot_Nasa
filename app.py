from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

# Credenciales de la API de Meteomatics
username = 'gonzalesastoray_andreaabigail'
password = '6DEsh48vL8'

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de FastAPI"}

# Endpoint para obtener la temperatura
@app.get("/weather/temperature")
def get_temperature(lat: float, lon: float):
    url = f"https://{username}:{password}@api.meteomatics.com/now/t_2m:C/{lat},{lon}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data['data'][0]['coordinates'][0]['dates'][0]['value'],
            "unit": "Celsius",
            "location": {
                "latitude": lat,
                "longitude": lon
            }
        }
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")

# Endpoint para obtener la precipitación
@app.get("/weather/precipitation")
def get_precipitation(lat: float, lon: float):
    url = f"https://{username}:{password}@api.meteomatics.com/now/precip_24h:mm/{lat},{lon}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "precipitation": data['data'][0]['coordinates'][0]['dates'][0]['value'],
            "unit": "mm",
            "location": {
                "latitude": lat,
                "longitude": lon
            }
        }
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")

# Endpoint para obtener la velocidad del viento
@app.get("/weather/wind_speed")
def get_wind_speed(lat: float, lon: float):
    url = f"https://{username}:{password}@api.meteomatics.com/now/wind_speed_10m:kmh/{lat},{lon}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "wind_speed": data['data'][0]['coordinates'][0]['dates'][0]['value'],
            "unit": "km/h",
            "location": {
                "latitude": lat,
                "longitude": lon
            }
        }
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")

# Endpoint para obtener la humedad del suelo
@app.get("/weather/soil_moisture")
def get_soil_moisture(lat: float, lon: float):
    url = f"https://{username}:{password}@api.meteomatics.com/now/soil_moisture_0_1m:percent/{lat},{lon}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "soil_moisture": data['data'][0]['coordinates'][0]['dates'][0]['value'],
            "unit": "percent",
            "location": {
                "latitude": lat,
                "longitude": lon
            }
        }
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")

# Endpoint para obtener la radiación solar
@app.get("/weather/solar_radiation")
def get_solar_radiation(lat: float, lon: float):
    url = f"https://{username}:{password}@api.meteomatics.com/now/global_rad:W/{lat},{lon}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "solar_radiation": data['data'][0]['coordinates'][0]['dates'][0]['value'],
            "unit": "W/m²",
            "location": {
                "latitude": lat,
                "longitude": lon
            }
        }
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")
