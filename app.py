from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime

# Credenciales de la API de Meteomatics
username = 'gonzalesastoray_andreaabigail'
password = '6DEsh48vL8'

# URL base para hacer las peticiones
base_url = f'https://{username}:{password}@api.meteomatics.com'

app = FastAPI()

# Función para obtener datos de la API de Meteomatics
def get_meteomatics_data(lat: float, lon: float, params: str):
    date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')  # Fecha actual UTC en formato ISO 8601
    url = f'{base_url}/{date}/{params}/{lat},{lon}/json'
    response = requests.get(url)
    
    # Asegúrate de devolver siempre un JSON válido
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos de Meteomatics")

# Endpoint para obtener la temperatura en JSON
@app.get("/weather/temperature")
def get_temperature(lat: float, lon: float):
    params = 't_2m:C'
    data = get_meteomatics_data(lat, lon, params)
    
    # Asegurando que la respuesta sea en formato JSON
    return {
        "temperature": data['data'][0]['coordinates'][0]['dates'][0]['value'],
        "unit": "Celsius",
        "location": {
            "latitude": lat,
            "longitude": lon
        }
    }

# Endpoint para obtener la precipitación en JSON
@app.get("/weather/precipitation")
def get_precipitation(lat: float, lon: float):
    params = 'precip_24h:mm'
    data = get_meteomatics_data(lat, lon, params)
    
    return {
        "precipitation": data['data'][0]['coordinates'][0]['dates'][0]['value'],
        "unit": "mm",
        "location": {
            "latitude": lat,
            "longitude": lon
        }
    }

# Endpoint para obtener la velocidad del viento en JSON
@app.get("/weather/wind_speed")
def get_wind_speed(lat: float, lon: float):
    params = 'wind_speed_10m:kmh'
    data = get_meteomatics_data(lat, lon, params)
    
    return {
        "wind_speed": data['data'][0]['coordinates'][0]['dates'][0]['value'],
        "unit": "km/h",
        "location": {
            "latitude": lat,
            "longitude": lon
        }
    }

# Endpoint para obtener la humedad del suelo en JSON
@app.get("/weather/soil_moisture")
def get_soil_moisture(lat: float, lon: float):
    params = 'soil_moisture_0_1m:percent'
    data = get_meteomatics_data(lat, lon, params)
    
    return {
        "soil_moisture": data['data'][0]['coordinates'][0]['dates'][0]['value'],
        "unit": "percent",
        "location": {
            "latitude": lat,
            "longitude": lon
        }
    }

# Endpoint para obtener la radiación solar en JSON
@app.get("/weather/solar_radiation")
def get_solar_radiation(lat: float, lon: float):
    params = 'global_rad:W'
    data = get_meteomatics_data(lat, lon, params)
    
    return {
        "solar_radiation": data['data'][0]['coordinates'][0]['dates'][0]['value'],
        "unit": "W/m²",
        "location": {
            "latitude": lat,
            "longitude": lon
        }
    }
