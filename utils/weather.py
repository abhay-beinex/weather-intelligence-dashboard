import requests

def get_weather(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&forecast_days=7"
        f"&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()