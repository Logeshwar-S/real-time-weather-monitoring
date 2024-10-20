import requests

# Function to fetch current weather data from OpenWeatherMap API using city name
def fetch_weather_data(city, api_key):
    """
    Fetches current weather data from OpenWeatherMap API for a given city.
    
    Args:
        city (str): The name of the city for which weather data is being requested.
        api_key (str): The API key for authenticating the OpenWeatherMap API request.

    Returns:
        dict: The weather data in JSON format if the request is successful.
        None: If the request fails or encounters an error.
    """
    try:
        # Construct the API URL with the city name, API key, and metric units (Celsius)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Make a GET request to the API
        response = requests.get(url)
        
        # Check if the response status is successful (HTTP status code 200)
        if response.status_code == 200:
            return response.json()  # Return the weather data in JSON format
        else:
            # Log the status code and response message if the request fails
            print(f"Failed to fetch weather data for {city}: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        # Catch any network-related errors such as timeouts, DNS failures, etc.
        print(f"Network error occurred while fetching weather data for {city}: {e}")
        return None
    except Exception as e:
        # Catch any other unforeseen errors
        print(f"An unexpected error occurred while fetching weather data for {city}: {e}")
        return None
