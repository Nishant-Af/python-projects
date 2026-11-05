import requests
import json
import win32com.client as wincom

# for female voice 
# speaker = wincom.Dispatch("SAPI.SpVoice")
speak = wincom.Dispatch("SAPI.SpVoice")

voices = speak.GetVoices()

for voice in voices:
    if "Zira" in voice.GetDescription():
        speak.Voice = voice
        break
# speaker.Speak("Hello, this is the female voice.")


API_KEY = "YOUR__API__KEY__HERE"
# Get API_KEY from --> https://www.weatherapi.com/

city = input("Enter Name of Your City Sir : ")

URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

r = requests.get(URL)
# print(r.text)
weather_dic = json.loads(r.text)
country_details = f"The Country is {weather_dic["location"]["country"]} and the city is {city}"
temperature_detail = f"The Temperature in {city} is {weather_dic["current"]["temp_c"]} degrees Celcius"
wind_details = f"The Speed of wind in {city} is {weather_dic['current']['wind_kph']} kph"
rain_details = f"The Chance of snow in {city} is {weather_dic['current']['chance_of_snow']}"
snow_details = f"The Chance of rain in {city} is {weather_dic['current']['chance_of_rain']}"
humidity_details = f"The chance of humidity in {city} is {weather_dic['current']['humidity']}"
speak.speak(country_details)
speak.speak(temperature_detail)
speak.speak(wind_details)
speak.speak(rain_details)
speak.speak(snow_details)
speak.speak(humidity_details)