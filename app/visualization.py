import matplotlib
matplotlib.use('Agg')  # Use Agg backend for rendering plots
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_temperature_trends(weather_summaries):
    """
    Plots the temperature trends including average, minimum, and maximum temperatures,
    along with dominant weather conditions for each date.

    Args:
        weather_summaries (list of dict): A list of weather summary records, 
                                           each containing date, avg_temperature, 
                                           min_temperature, max_temperature, 
                                           and dominant_condition.
    """
    # Check if any weather summaries are provided for plotting
    if not weather_summaries:
        print("No weather summaries provided for plotting.")
        return

    try:
        # Extract and convert date strings to datetime objects
        dates = [datetime.strptime(entry['date'], '%Y-%m-%d %H:%M:%S') for entry in weather_summaries]
        avg_temperatures = [entry.get('avg_temperature') for entry in weather_summaries]
        min_temperatures = [entry.get('min_temperature') for entry in weather_summaries]
        max_temperatures = [entry.get('max_temperature') for entry in weather_summaries]
        conditions = [entry.get('dominant_condition') for entry in weather_summaries]

        # Create a new figure for plotting
        plt.figure(figsize=(10, 6))

        # Plot average, minimum, and maximum temperatures
        plt.plot(dates, avg_temperatures, marker='o', color='b', label='Avg Temperature')
        plt.plot(dates, min_temperatures, marker='x', linestyle='--', color='g', label='Min Temperature')
        plt.plot(dates, max_temperatures, marker='x', linestyle='--', color='r', label='Max Temperature')

        # Annotate the plot with dominant weather conditions
        for i, condition in enumerate(conditions):
            plt.annotate(condition, (dates[i], avg_temperatures[i]), 
                         textcoords="offset points", xytext=(0, 10), ha='center')

        # Formatting the x-axis to display dates properly
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

        # Set plot titles and labels
        plt.title("Temperature Trends with Weather Conditions")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.legend()

        # Adjust layout to prevent clipping of tick-labels
        plt.tight_layout()

        # Save the figure to a PNG file
        filename = f'temperature_trends_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        plt.savefig(filename)
        plt.close()  # Close the plot to free memory
        print(f"Temperature trends plot saved as '{filename}'.")

    except Exception as e:
        print(f"Error while plotting temperature trends: {e}")
