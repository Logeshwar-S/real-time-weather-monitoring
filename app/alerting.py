from mysql.connector import Error
from config import TEMP_THRESHOLD, ALERT_CONSECUTIVE_THRESHOLD

# Dictionary to track consecutive alert breaches for each city
consecutive_alerts = {}

# Function to check if the current temperature exceeds the defined threshold
# and trigger an alert if the condition is met for consecutive updates
def check_temperature_alert(connection, city, current_temp):
    """
    Checks if the temperature in a specific city exceeds the predefined threshold 
    for a consecutive number of updates. If the threshold is exceeded for 
    consecutive times, an alert is triggered.

    Args:
        connection (object): MySQL connection object for database operations.
        city (str): Name of the city for which temperature is being checked.
        current_temp (float): The latest temperature reading for the city.

    Returns:
        None
    """
    
    # Initialize the alert counter for the city if it's not already tracked
    if city not in consecutive_alerts:
        consecutive_alerts[city] = 0

    # Check if the current temperature exceeds the threshold
    if current_temp > TEMP_THRESHOLD:
        consecutive_alerts[city] += 1  # Increment the consecutive alert counter

        # Trigger an alert if the threshold is breached for consecutive updates
        if consecutive_alerts[city] >= ALERT_CONSECUTIVE_THRESHOLD:
            print(f"ALERT: Temperature in {city} has exceeded the threshold of {TEMP_THRESHOLD}°C "
                  f"for {ALERT_CONSECUTIVE_THRESHOLD} consecutive updates!")
            insert_alert(connection, city, current_temp)  # Insert the alert into the database
    else:
        # Reset the counter if the temperature is below the threshold
        consecutive_alerts[city] = 0

# Function to insert triggered alerts into the 'weather_alerts' table in the database
def insert_alert(connection, city, current_temp):
    """
    Inserts a weather alert into the 'weather_alerts' table in the database.

    Args:
        connection (object): MySQL connection object for database operations.
        city (str): Name of the city for which the alert is triggered.
        current_temp (float): The temperature that triggered the alert.

    Returns:
        None
    """
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO weather_alerts (city, temperature, alert_time)
        VALUES (%s, %s, NOW())
        """
        cursor.execute(insert_query, (city, current_temp))
        connection.commit()
        print(f"Alert for {city} inserted successfully.")
    except Error as e:
        print(f"Error inserting alert: {e}")
    finally:
        cursor.close()  # Ensure the cursor is closed to prevent memory leaks
