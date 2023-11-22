import tkinter
from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

primary_color = "#3B6978"  # Dark blue
secondary_color = "#F9BC60"  # Light orange
text_color = "#FFFFFF"  # White text
bg_color = "#E0FBFC"  # Light blue background

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(api_key, city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    data = response.json()
    return data

# Function to display weather information in a messagebox
def display_weather_data(city_name):
    api_key = '5d860afe17c13910e7cb5bae6eec274c'
    weather_data = get_weather_data(api_key, city_name)
    # Check if the API response is successful
    if weather_data['cod'] == 200:
        main_data = weather_data['main']
        weather = weather_data['weather'][0]['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        # Construct weather information text
        result_text = f"Weather in {city_name}: {weather}\nTemperature: {temperature} °C\nHumidity: {humidity}%"
        # Show weather information in a messagebox
        messagebox.showinfo("Weather Information", result_text)
        # Add the city to the recent searches list
        add_to_recent_searches(city_name)
    else:
        # Show error message if the city name is invalid or API request fails
        messagebox.showerror("Error", "Please input a valid City Name!")

# Function to add city to the recent searches list
def add_to_recent_searches(city_name):
    recent_searches.insert(0, city_name)

# Function triggered by the "Get Weather" button
def get_weather_info():
    city_name = entry.get()
    display_weather_data(city_name)

height = 800
width  = 400

# Updated color scheme
primary_color = "#3B6978"  # Dark blue
secondary_color = "#B0A695"  # Light orange
text_color = "#FFFFFF"  # White text
bg_color = "#E0FBFC"  # Light blue background

# Window setup
window = Tk()
window.title("Weather App")
window.geometry("800x400")
window.configure(bg=bg_color)

# Header label
label = Label(window, font=("Times New Roman", 50), text="Weather Detector", bg=primary_color, fg=text_color)
label.pack(fill='x')

# Label for city name entry
label = Label(window, font=("Roboto", 20, "bold"), text="Enter City Name: ", bg=bg_color, fg=primary_color)
label.pack(pady=20)

# Entry for city name
entry = Entry(window, bg=secondary_color, fg=primary_color)
entry.pack(padx=10)

# Button for weather information
button = Button(window, text="Get Weather", command=get_weather_info, bg=secondary_color, fg=primary_color)
button.pack(pady=10)

# Label for recent searches
recent_searches_label = Label(window, font=("Times New Roman", 20, "bold"), text="Recent Searches:", bg=bg_color, fg=primary_color)
recent_searches_label.pack(pady=10)

# Listbox for recent searches
recent_searches = Listbox(window, font=("Arial", 12), selectmode=SINGLE, height=5, bg=secondary_color, fg=primary_color)
recent_searches.pack(padx=10)

window.mainloop()
