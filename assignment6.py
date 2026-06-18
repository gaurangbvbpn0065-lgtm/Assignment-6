import requests
import random
from datetime import datetime

# -----------------------------------------
# 1. OpenWeather API
# -----------------------------------------

API_KEY = "YOUR_OPENWEATHER_API_KEY"   # Replace with your API key
CITY = "Jaipur"

print("=" * 50)
print("OPEN WEATHER API DATA")
print("=" * 50)

try:
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()

        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Minimum Temp:", data["main"]["temp_min"], "°C")
        print("Maximum Temp:", data["main"]["temp_max"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Pressure:", data["main"]["pressure"], "hPa")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        print("Sunrise:", sunrise.strftime("%H:%M:%S"))
        print("Sunset:", sunset.strftime("%H:%M:%S"))

    else:
        print("Invalid API Key or City Name")

except Exception as e:
    print("Error:", e)

# -----------------------------------------
# 2. Today's Game (Number Guessing Game)
# -----------------------------------------

print("\n" + "=" * 50)
print("NUMBER GUESSING GAME")
print("=" * 50)

number = random.randint(1, 20)

for attempt in range(5):

    guess = int(input("Guess a number between 1 and 20: "))

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess < number:
        print("Too Low!")

    else:
        print("Too High!")

else:
    print("Game Over!")
    print("Correct Number was:", number)

# -----------------------------------------
# 3A. Random User API
# -----------------------------------------

print("\n" + "=" * 50)
print("RANDOM USER API")
print("=" * 50)

try:
    response = requests.get("https://randomuser.me/api/")

    if response.status_code == 200:
        user = response.json()["results"][0]

        print("Name:",
              user["name"]["title"],
              user["name"]["first"],
              user["name"]["last"])

        print("Gender:", user["gender"])
        print("Email:", user["email"])
        print("Country:", user["location"]["country"])
        print("Phone:", user["phone"])

except Exception as e:
    print("Error:", e)

# -----------------------------------------
# 3B. Bored API (Activity Suggestion)
# -----------------------------------------

print("\n" + "=" * 50)
print("BORED API")
print("=" * 50)

try:
    response = requests.get("https://www.boredapi.com/api/activity")

    if response.status_code == 200:
        activity = response.json()

        print("Suggested Activity:", activity["activity"])
        print("Type:", activity["type"])
        print("Participants:", activity["participants"])

except Exception as e:
    print("Error:", e)