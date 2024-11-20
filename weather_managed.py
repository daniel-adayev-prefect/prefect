from prefect import flow, task, runtime




@flow
def fetch_weather_v2():
    url = "https://api.open-meteo.com/v1/forecast"
    print(url)
    return url

