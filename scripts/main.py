# scripts/main.py

from app.api_client import fetch_weather_data
from app.data_processing import process_weather_data, add_to_daily_summary, get_daily_summaries
from app.database import create_connection, insert_weather_summary, close_connection
from app.alerting import check_temperature_alert
from app.visualization import plot_temperature_trends
from config import API_KEY, CITIES, SLEEP_INTERVAL
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up the connection to MySQL
connection = create_connection()

def main():
    """
    Main function to fetch weather data for configured cities, process it, 
    store it in the database, check for temperature alerts, and plot trends.
    """
    weather_summaries = []  # List to hold summaries for plotting

    # Dictionary to hold daily summaries for all cities
    daily_summaries_dict = {}

    # Iterate through each city to fetch and process weather data
    for city in CITIES:
        logging.info(f"Fetching weather data for {city}...")
        data = fetch_weather_data(city, API_KEY)  # Fetch weather data using the API key
        
        if data:
            processed_data = process_weather_data(data)  # Process the fetched weather data
            
            if processed_data:
                # Log processed data for debugging
                logging.info(f"Processed data for {city}: {processed_data}")

                # Add processed data to the daily summary for the city
                add_to_daily_summary(processed_data['city'], processed_data)

                # Insert the processed data into the database
                insert_weather_summary(
                    connection,
                    processed_data['city'],
                    processed_data['date'],  # Insert the correctly formatted date
                    processed_data['temperature'],
                    processed_data['max_temperature'],
                    processed_data['min_temperature'],
                    processed_data['weather_condition']
                )

                # Collect processed data for plotting
                weather_summaries.append({
                    'date': processed_data['date'],
                    'avg_temperature': processed_data['temperature']  # Use the processed temperature
                })

                # Check for temperature alerts based on current temperature
                check_temperature_alert(connection, processed_data['city'], processed_data['temperature'])

                # Collect daily summaries for this city
                daily_summary = get_daily_summaries(processed_data['city'])
                if daily_summary:
                    daily_summaries_dict[processed_data['city']] = daily_summary

    # Log the daily summaries collected for all cities
    for city, summary in daily_summaries_dict.items():
        logging.info(f"Daily summary for {city}: {summary}")

    # Plot temperature trends after fetching data for all cities
    plot_temperature_trends(weather_summaries)

if __name__ == "__main__":
    try:
        while True:
            main()  # Execute the main function
            time.sleep(SLEEP_INTERVAL)  # Wait for the specified interval before the next update
    except KeyboardInterrupt:
        logging.info("Stopping weather monitoring...")  # Gracefully handle script termination
    finally:
        close_connection(connection)  # Close the database connection
