import requests
import json

api_key = 'your api key here'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter City Name: ")

url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temp = y["temp"]
    temperature = round(current_temp - 273.15)
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    
    z = x["weather"]
    description = z[0] ["description"]
    
    print("Temperature : ", str(temperature),"°C")
    print("Atmospheric Pressure: ", str(current_pressure),"hpa")
    print("Humidity : ", str(current_humidity),"%")
    print("Description : ", str(description))
   
else: 
    print("City not found!!")