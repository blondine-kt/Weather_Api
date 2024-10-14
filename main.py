from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn
load_dotenv()

app = FastAPI()

def getWeather():
    
    #wether Api url
    weatherApi = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Montreal?unitGroup=metric&key=J5MMVZLHCQJJYQJB6LF7546WY&contentType=json'

    try:

        #request to weather Api
        response = requests.get(weatherApi)

        info = response.json()

        #extract required information

        return info 
    
    except Exception as e:
        print(e)


@app.get("/weather_info")
async def get_weather_info():

    #retourne l'info sur la meteo
    weather = getWeather()

    return weather


if __name__ =='__main__':
     uvicorn.run(app, host='0.0.0.0', port =8040, workers=1)

