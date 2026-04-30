from send_text import text_alert
from dotenv import load_dotenv
import schedule
import requests
import time

load_dotenv()

def get_weather(latitude, longitude):
    base_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max"
        f"&current=temperature_2m"
        f"&timezone=America%2FChicago"
        f"&temperature_unit=fahrenheit"
    )

    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Weather API Error: ", e)
        return None
    
def send_weather_update():
    print("Weathering...")
    #change location here
    latitude = 36.3878
    longitude = -86.4485

    weather_data = get_weather(latitude, longitude)

    if not weather_data or "current" not in weather_data:
        print("Weather Failed")
        return

    temp = weather_data["current"]["temperature_2m"]
    high_temp = weather_data["daily"]["temperature_2m_max"][0]

    weather_info = (
        f"Good Morning!\n"
        f"Current: {temp:.1f}˚F\n"
        f"High Today: {high_temp:.1f}˚F\n"
        f"Have A Great Day!\n"
    )

    text_alert(
        subject="Weather Update",
        body=weather_info,
    )

def main():
    #change time here
    schedule.every().day.at("06:00").do(send_weather_update)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    #send_weather_update()