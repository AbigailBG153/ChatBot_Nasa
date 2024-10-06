import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionProveerTemperatura(Action):
    def name(self):
        return "action_proveer_temperatura"

    def run(self, dispatcher, tracker, domain):
        username = 'gonzalesastoray_andreaabigail'
        password = '6DEsh48vL8'
        url = "https://{}:{}@api.meteomatics.com/now/t_2m:C/13.52,-71.97/json".format(username, password)

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data['data'][0]['coordinates'][0]['dates'][0]['value']
            dispatcher.utter_message(text=f"La temperatura actual es {temperatura}°C.")
            return [SlotSet("temperatura", temperatura)]
        else:
            dispatcher.utter_message(text="Lo siento, no pude obtener la temperatura.")
            return []

class ActionProveerViento(Action):
    def name(self):
        return "action_proveer_viento"

    def run(self, dispatcher, tracker, domain):
        username = 'gonzalesastoray_andreaabigail'
        password = '6DEsh48vL8'
        url = "https://{}:{}@api.meteomatics.com/now/wind_speed_10m:ms,wind_dir_10m:d/13.52,-71.97/json".format(username, password)

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            velocidad_viento = data['data'][0]['coordinates'][0]['dates'][0]['value']
            direccion_viento = data['data'][1]['coordinates'][0]['dates'][0]['value']
            viento = f"{velocidad_viento} m/s, dirección {direccion_viento}°"
            dispatcher.utter_message(text=f"La velocidad del viento es {viento}.")
            return [SlotSet("viento", viento)]
        else:
            dispatcher.utter_message(text="Lo siento, no pude obtener la velocidad del viento.")
            return []

class ActionProveerHumedad(Action):
    def name(self):
        return "action_proveer_humedad"

    def run(self, dispatcher, tracker, domain):
        username = 'gonzalesastoray_andreaabigail'
        password = '6DEsh48vL8'
        url = "https://{}:{}@api.meteomatics.com/now/humidity_2m:p/13.52,-71.97/json".format(username, password)

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            humedad = data['data'][0]['coordinates'][0]['dates'][0]['value']
            dispatcher.utter_message(text=f"La humedad actual es {humedad}%.")
            return [SlotSet("humedad", humedad)]
        else:
            dispatcher.utter_message(text="Lo siento, no pude obtener la humedad.")
            return []

class ActionProveerPrecipitacion(Action):
    def name(self):
        return "action_proveer_precipitacion"

    def run(self, dispatcher, tracker, domain):
        username = 'gonzalesastoray_andreaabigail'
        password = '6DEsh48vL8'
        url = "https://{}:{}@api.meteomatics.com/now/precip_1h:mm/13.52,-71.97/json".format(username, password)

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            precipitacion = data['data'][0]['coordinates'][0]['dates'][0]['value']
            dispatcher.utter_message(text=f"La precipitación es {precipitacion} mm.")
            return [SlotSet("precipitacion", precipitacion)]
        else:
            dispatcher.utter_message(text="Lo siento, no pude obtener la precipitación.")
            return []
