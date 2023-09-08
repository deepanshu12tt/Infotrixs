import requests
import time


API_KEY = '49c7e5c2c5344ce8b16175043230209'

API_BASE_URL = "http://api.weatherapi.com/"
favorite_cities = []

# Function to fetch weather data for a city
def get_weather(city_name):

    #url = f"{API_BASE_URL}/v1/current.json?key={API_KEY}&q={city_name}&aqi=no"
    url= f"http://api.weatherapi.com/v1/current.json?key=49c7e5c2c5344ce8b16175043230209&q={city_name}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:

        content_type = response.headers.get('Content-Type', '').lower()

        if 'application/json' in content_type:
            weather_data = response.json()
            print(f"Weather in {city_name}:")
            print(f"Temperature: {weather_data['current']['temp_c']}°C")
            print(f"Condition: {weather_data['current']['condition']['text']}")
        else:
            # Handle HTML response
            print(f"Received HTML response for {city_name}:")
            print(response.text)
    else:
        print(f"Error fetching weather data for {city_name}")
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")


def add_favorite(city_name):
    if city_name not in favorite_cities:
        favorite_cities.append(city_name)
        print(f"{city_name} added to favorites.")
    else:
        print(f"{city_name} is already in your favorites.")

def remove_favorite(city_name):
    if city_name in favorite_cities:
        favorite_cities.remove(city_name)
        print(f"{city_name} removed from favorites.")
    else:
        print(f"{city_name} is not in your favorites.")

def list_favorites():
    print("Your favorite cities:")
    for city in favorite_cities:
        print(city)




while True:
        print("\nOptions:")
        print("1. Check weather by city name")
        print("2. Add a city to favorites")
        print("3. Remove a city from favorites")
        print("4. List favorite cities")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter city name: ")
            get_weather(city_name)
        elif choice == "2":
            city_name = input("Enter city name to add to favorites: ")
            add_favorite(city_name)
        elif choice == "3":
            city_name = input("Enter city name to remove from favorites: ")
            remove_favorite(city_name)
        elif choice == "4":
            list_favorites()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        refresh_interval = 15 + int(time.time()) % 13
        print(f"Refreshing in {refresh_interval} seconds...")
        time.sleep(refresh_interval)
