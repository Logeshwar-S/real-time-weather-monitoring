# config.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file for better security
load_dotenv()

# OpenWeatherMap API key
API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Fetch from environment variables

# Cities to monitor (metros in India)
CITIES = [
    'Delhi',
    'Mumbai',
    'Chennai',
    'Bangalore',
    'Kolkata',
    'Hyderabad'
]

# Temperature thresholds for alerts
TEMP_THRESHOLD = 35.0  # Alert when temperature exceeds 35°C
ALERT_CONSECUTIVE_THRESHOLD = 2  # Trigger alert if breached in 2 consecutive updates

# Interval to wait between data fetches (in seconds)
SLEEP_INTERVAL = 300  # 5 minutes

# Optional: Add more configurations as needed

def display_config():
    """
    Displays the current configuration settings.
    This can help during debugging or when verifying settings.
    """
    print("Current Configuration:")
    print(f"API Key: {'*****' if API_KEY else 'Not Set'}")  # Hide API key for security
    print(f"Cities to Monitor: {', '.join(CITIES)}")
    print(f"Temperature Alert Threshold: {TEMP_THRESHOLD}°C")
    print(f"Alert Consecutive Threshold: {ALERT_CONSECUTIVE_THRESHOLD} updates")
    print(f"Sleep Interval: {SLEEP_INTERVAL} seconds")

if __name__ == "__main__":
    # Display the configuration when this script is run directly
    display_config()
