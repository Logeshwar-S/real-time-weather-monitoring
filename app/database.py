import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Establishes a connection to the MySQL database.
    
    Returns:
        connection (mysql.connector.connection.MySQLConnection): The connection object if successful.
        None: If the connection fails.
    """
    try:
        # Create a MySQL connection using the provided credentials
        connection = mysql.connector.connect(
            host='localhost',         # Database host
            database='weather_monitoring',  # Name of the database
            user='admin',             # Replace with your MySQL username
            password='password'       # Replace with your MySQL password
        )
        
        # Check if the connection is successful
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    
    except Error as e:
        # Print an error message if connection fails
        print(f"Error while connecting to MySQL: {e}")
        return None

def insert_weather_summary(connection, city, date, avg_temp, max_temp, min_temp, weather_condition):
    """
    Inserts a weather summary record into the weather_summary table.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object.
        city (str): The name of the city.
        date (str): The date and time of the weather summary (in 'YYYY-MM-DD HH:MM:SS' format).
        avg_temp (float): The average temperature for the day.
        max_temp (float): The maximum temperature recorded.
        min_temp (float): The minimum temperature recorded.
        weather_condition (str): The dominant weather condition for the day.
    """
    try:
        cursor = connection.cursor()

        # SQL query to insert weather data into the weather_summary table
        insert_query = """
        INSERT INTO weather_summary (city, date, avg_temperature, max_temperature, min_temperature, weather_condition)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Execute the insert operation with provided values
        cursor.execute(insert_query, (city, date, avg_temp, max_temp, min_temp, weather_condition))
        connection.commit()

        # Confirmation message after a successful insertion
        print(f"Weather summary for {city} inserted successfully.")
    
    except Error as e:
        # Print an error message if something goes wrong during insertion
        print(f"Error inserting weather summary: {e}")
    
    finally:
        cursor.close()  # Close the cursor to free up resources

def get_weather_summaries(connection, city):
    """
    Fetches the last 10 weather summaries for a specified city from the weather_summary table.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object.
        city (str): The name of the city.

    Returns:
        rows (list of dict): A list of the most recent 10 weather summaries for the city.
        None: If an error occurs during the fetch.
    """
    try:
        cursor = connection.cursor(dictionary=True)  # Fetch data as a dictionary for better readability

        # SQL query to select the most recent 10 weather summaries for a specific city
        select_query = """
        SELECT * FROM weather_summary WHERE city = %s ORDER BY date DESC LIMIT 10
        """

        # Execute the query and fetch the results
        cursor.execute(select_query, (city,))
        rows = cursor.fetchall()

        return rows  # Return the list of summaries
    
    except Error as e:
        # Print an error message if the fetch operation fails
        print(f"Error fetching weather summaries: {e}")
        return None

    finally:
        cursor.close()  # Close the cursor to free up resources

def close_connection(connection):
    """
    Closes the connection to the MySQL database.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object.
    """
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
