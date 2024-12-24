from dotenv import load_dotenv
import py5

import datetime as dt
import requests
import os

now = dt.datetime.now()



load_dotenv()

geolocation_response = requests.get("http://ip-api.com/json/")
geolocation_json = geolocation_response.json()


weather_api_key = os.getenv("OPENWEATHERMAP_KEY")
weather_api_link = "https://api.openweathermap.org/data/2.5/weather"
weather_api_params = {
    "lat" : geolocation_json["lat"],
    "lon" : geolocation_json["lon"],
    "appid" : weather_api_key,
    "units" : "metric"
}
weather_response = requests.get(weather_api_link, weather_api_params)
weather_json = weather_response.json()

for symbol in now.strftime("%H:%M"):
    print(symbol)

temp    = round(weather_json['main']['temp'])
temp_fl = round(weather_json['main']['feels_like'])
print(f"{temp} °C. FEELS LIKE {temp_fl} °C")

def setup():
    py5.size(1280, 720)
    # py5.full_screen()

    global font_main 
    font_main = py5.create_font("Arial Bold", 256)

    py5.no_stroke()


TIME_X = 241
TIME_W = 117
TIME_Y_STEP = 80
INFO_X = TIME_X + TIME_W + 70
INFO_H = 50

def draw():
    py5.background(0xFF, 0xD1, 0x66)

    

    py5.fill(0xEF, 0x47, 0x6F)
    py5.rect(TIME_X, 0, TIME_W, py5.height)
    py5.rect(358, 73, 750, INFO_H)
    py5.rect(358, 221, 650, INFO_H)
    py5.rect(358, 374, 550, INFO_H)
    py5.rect(358, 539, 450, INFO_H)

    py5.fill(0x26, 0x54, 0x7C)
    py5.text_font(font_main)
    py5.text_size(70)
    py5.text_align(py5.CENTER, py5.CENTER)

    now = dt.datetime.now()
    time = now.strftime("%H:%M")
    for i, symbol in enumerate(time):
        py5.text(symbol, TIME_X + TIME_W / 2, py5.height / 2 + TIME_Y_STEP * (i - 2))

    py5.text_size(29)
    py5.text_align(py5.LEFT, py5.CENTER)

    py5.text("CLEAR. NO PRECIPITATION IS EXPECTED.", INFO_X, 73 + INFO_H / 2)


    py5.text("EUROPE. RUSSIA. MOSCOW. RU", INFO_X, 221 + INFO_H / 2)
    py5.text("+6 °C. FEELS LIKE +3 °C", INFO_X, 374 + INFO_H / 2)
    py5.text("DECEMBER 24 2024", INFO_X, 539 + INFO_H / 2)

   
   

py5.run_sketch()

