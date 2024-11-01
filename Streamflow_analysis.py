import pandas as pd
import matplotlib.pyplot as plt

# Definig the path streamflow data of my staion
file_path = r'D:\Python_Practice\Streamflow_Visualization\Daily_Streamflow2010.xlsx'

# enable to read read the Excel file
data = pd.read_excel(file_path)

# Now showing the first few rows of the dataframe to verify the structure
print(data.head())
print("Column names:", data.columns)

# Ensure the 'Date' column is of datetime type
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Set the 'Date' as the index
data.set_index('Date', inplace=True)

# Calculate the mean monthly discharge
monthly_mean = data['Discharge (Cumics)'].resample('M').mean()

# Plotting the mean monthly discharge
plt.figure(figsize=(12, 6))
monthly_mean.plot(kind='bar', color='lightblue')
plt.title('Mean Monthly Discharge at Khairtabad Station (2010)', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Mean Discharge (cubic meters per second)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

# Save the plot to a file
plt.savefig(r'D:\Python_Practice\Streamflow_Visualization\Mean_Monthly_Discharge.png')
plt.show()
# Plotting the daily discharge data
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Discharge (Cumics)'], color='blue', linewidth=1)
plt.title('Daily Discharge at Khairtabad Station (2010)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Discharge (Cumecs)', fontsize=14)
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Save the plot to a file
plt.savefig(r'D:\Python_Practice\Streamflow_Visualization\Daily_Discharge.png')
plt.show()
