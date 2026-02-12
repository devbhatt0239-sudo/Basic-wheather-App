import requests

print("===================================")
print("        BASIC WEATHER APP          ")
print("===================================")

api_key = "c34b77af7ef958c4edc7afcb007c2f41"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("City not found!")
    else:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nWeather Details")
        print("----------------------------")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

except:
    print("Error: Check internet or API key")
