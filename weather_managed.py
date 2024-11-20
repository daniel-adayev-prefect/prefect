from prefect import flow, task, runtime
import httpx
import random
from prefect.blocks.system import JSON
from prefect.artifacts import create_markdown_artifact



@task(retries=4)
def generate_random_coordinates():
    print(runtime.task_run.name)
    json_block = JSON.load("weight")
    print("json block" + ": " + str(json_block))
    latitude = random.uniform(-90, 90)  # Random latitude between -90 and 90
    longitude = random.uniform(-180, 180)  # Random longitude between -180 and 180
    return latitude, longitude

@flow
def fetch_weather() -> dict:
    latitude, longitude = generate_random_coordinates()
    print(latitude, longitude)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": latitude, "longitude": longitude, "hourly": "temperature_2m"}
    response = httpx.get(url, params=params)
    x = response.json()['hourly']
    for time, temp in zip(x['time'],x['temperature_2m']) :
        print(str(time) + ' --> ' + str(temp))
    return response.json()

