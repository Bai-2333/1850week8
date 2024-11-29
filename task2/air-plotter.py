'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = 't2-graph/leeds-centre-air-quality.csv'

# Load the CSV file
def plot_air_quality(file_path):
    try:
        # Read the data into a DataFrame
        data = pd.read_csv(file_path)

        # Calculate the average of the four values (pm25, pm10, o3, no2) ;list=['pm25', 'pm10', 'o3', 'no2']
        data['Average Pollution'] = data[['pm25', 'pm10', 'o3', 'no2']].mean(axis=1) # calculate the average values along row, axis=1;

        # Convert the 'date' column to datetime format for better plotting
        data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y') # day,month,year

        # Plot the data
        plt.figure(figsize=(12, 6))
        plt.plot(data['date'], data['Average Pollution'], marker='o', linestyle='-', color='blue', label='Average Pollution')

        # Add title, labels, and grid
        plt.title("Average Air Quality Pollution - Mingjiang Bai", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Average Pollution", fontsize=14)
        plt.xticks(rotation=45) #rotation=60/90
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()

        # Show the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


# Plot the air quality data
plot_air_quality(file_path)


