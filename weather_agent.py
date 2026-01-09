import requests
from api_keys.config import OPENWEATHER_API_KEY

def get_weather(location: str) -> str:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            return f"❌ Error: {data.get('message', 'Unable to get weather')}"

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        city = data["name"]
        country = data["sys"]["country"]

        return f"🌤 {city}, {country}: {temp}°C ({weather_desc}, feels like {feels_like}°C)"
    
    except Exception as e:
        return f"❌ Exception: {str(e)}"
