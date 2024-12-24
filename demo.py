import threading
from time import sleep

import py5

import requests


def update_geolocation():
    while True:
        geolocation_response = requests.get("http://ip-api.com/json/")
        geolocation_json = geolocation_response.json()
        print(geolocation_json["lat"], geolocation_json["lon"])

        sleep(5)

geolocation_thread = threading.Thread(target=update_geolocation, daemon=True)



def setup():
    py5.size(720, 480)

    py5.fill(255)
    py5.no_stroke()

    geolocation_thread.start()

 
def draw():
    py5.background(0)
    py5.circle(py5.mouse_x, py5.mouse_y, 50)

   

py5.run_sketch()
