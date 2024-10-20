from collections import defaultdict
from datetime import datetime
import logging

# A dictionary to store weather data for daily rollups
daily_weather_data = defaultdict(lambda: {'temps': [], 'conditions': []})

def add_to_daily_summary(city, processed_data):
    """
    Adds the processed weather data to the daily rollup for the specified city.
    
    Args:
        city (str): The name of the city.
        processed_data (dict): The processed weather data, including temperature and condition.
    """
    global daily_weather_data  # Access the global dictionary
    daily_data = daily_weather_data[city]

    # Append the temperature and weather condition to the city's rollup
    daily_data['temps'].append(processed_data['temperature'])
    daily_data['conditions'].append(processed_data['weather_condition'])

def get_daily_summaries(city):
    """
    Retrieve the daily summary of weather data for a specific city.
    
    Args:
        city (str): The name of the city.

    Returns:
        dict: The summary data containing average, min, and max temperatures, and dominant weather condition.
        None: If no data exists for the specified city.
    """
    global daily_weather_data  # Access the global variable
    if city in daily_weather_data:
        data = daily_weather_data[city]
        
        if data['temps']:  # Ensure there's data to summarize
            avg_temp = sum(data['temps']) / len(data['temps'])
            max_temp = max(data['temps'])
            min_temp = min(data['temps'])

            # Calculate the most frequent weather condition (dominant condition)
            weather_count = defaultdict(int)
            for condition in data['conditions']:
                weather_count[condition] += 1
            dominant_condition = max(weather_count, key=weather_count.get)

            # Return the summary data
            return {
                'city': city,
                'avg_temperature': round(avg_temp, 2),
                'max_temperature': round(max_temp, 2),
                'min_temperature': round(min_temp, 2),
                'dominant_condition': dominant_condition
            }
    return None  # Return None if no data exists for the city

def process_weather_data(data):
    """
    Processes raw weather data fetched from the API into a more usable format.
    
    Args:
        data (dict): The raw weather data from the API.

    Returns:
        dict: The processed weather data with temperatures, conditions, and timestamp.
        None: If an error occurs during processing.
    """
    try:
        # Extract the relevant weather data fields
        city = data['name']
        weather_info = data['weather'][0]  # First weather condition

        # Temperatures are assumed to be in Celsius, as set in the API request
        temperature_celsius = data['main']['temp']
        min_temperature_celsius = data['main']['temp_min']
        max_temperature_celsius = data['main']['temp_max']

        # Log raw temperature details
        logging.info(f"Raw temperatures (C) for {city}: Temp: {temperature_celsius}, Min: {min_temperature_celsius}, Max: {max_temperature_celsius}")

        # Create the processed data dictionary
        processed_data = {
            'city': city,
            'temperature': round(temperature_celsius, 2),  # Round temperatures to two decimal places
            'min_temperature': round(min_temperature_celsius, 2),
            'max_temperature': round(max_temperature_celsius, 2),
            'weather_condition': weather_info['description'],  # Weather description
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
        }

        return processed_data

    except Exception as e:
        # Log any errors that occur during the data processing
        logging.error(f"Error processing weather data for {data.get('name', 'Unknown')}: {e}")
        return None

