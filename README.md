# Weather Monitoring System

## Overview

The Weather Monitoring System is a Python application that fetches weather data from the OpenWeatherMap API for various cities in India. It processes this data to monitor temperature trends, triggers alerts for extreme temperatures, and stores the results in a MySQL database. The application also visualizes the temperature trends over time.

## Features

- Fetches current weather data for specified cities.
- Alerts users when the temperature exceeds a defined threshold for consecutive updates.
- Stores weather summaries in a MySQL database.
- Provides daily summaries of weather data.
- Visualizes temperature trends using Matplotlib.

## Technologies Used

- Python
- OpenWeatherMap API
- MySQL
- Matplotlib
- dotenv for environment variable management

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- MySQL server
- Pip (Python package installer)

## Installation

1. Clone the repository:

```
   git clone https://github.com/Logeshwar-S/real-time-weather-monitoring.git
   cd weather-monitoring
```
2. Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install required packages:

```
pip install -r requirements.txt
```

4. Set up the MySQL database:

- Create a database named weather_monitoring.
- Run the SQL scripts in scripts/ directory to create necessary tables (weather_summary, weather_alerts, etc.).

5. Configure environment variables:
- Create a .env file in the root directory of your project and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

6. Update config.py with any additional configuration settings as needed.

## Usage
1. Run the application:

You can start the weather monitoring application by executing the following command:

```
python scripts/main.py
```
The application will continuously fetch weather data at the interval defined in config.py (default is 5 minutes).

2. Visualize Data: The application will automatically generate plots of temperature trends and save them as PNG files in the project directory.

3. View Alerts: Alerts will be printed to the console whenever the temperature exceeds the defined threshold for consecutive updates.


## Contributing
Contributions are welcome! If you have suggestions for improvements or features, please fork the repository and submit a pull request.

