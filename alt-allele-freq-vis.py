import pandas as pd
import pyexcel_ods
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame()


# Function to read .ods file and return DataFrame
def read_ods_to_dataframe(file_path):
    data = pyexcel_ods.get_data(file_path)
    sheet_data = data[list(data.keys())[0]]  # Assumes the first sheet
    df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])  # Assumes first row is header
    return df

# Load data from the provided ODS file
file_path = 'raw-spreadsheets/allele_freq_lon_plot.ods'
data = read_ods_to_dataframe(file_path)

# Print the first few rows of the original data
print("Original Data:")
print(data.head())

#Filter out cells with value 'NA'
data = data.dropna(subset=['snp'])

# Filter out rows where Lon_pre, Lon_dur, or Lon_post have values less than 0.4
filtered_data = data[(data['Lon_pre'] >= 0.4) & (data['Lon_dur'] >= 0.4) & (data['Lon_post'] >= 0.4)]

# Print the first few rows of the filtered data
print("Filtered Data:")
print(filtered_data.head(n=53))

# Define positions and width of bars
x = np.arange(len(filtered_data['snp']))  # the positions on the x-axis
width = 0.2  # Width of the bars on the plot

fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for each column
bars1 = ax.bar(x - width, filtered_data['Lon_pre'], width, label='Lon_pre', color='cornflowerblue')
bars2 = ax.bar(x, filtered_data['Lon_dur'], width, label='Lon_dur', color='brown')
bars3 = ax.bar(x + width, filtered_data['Lon_post'], width, label='Lon_post', color='darkseagreen')

# Labeling and layout
ax.set_xlabel('Snp')
ax.set_ylabel('Allele Frequency')
ax.set_title('Plot of Alternate Allele Frequency vs Snp')
ax.set_xticks(x)
ax.set_xticklabels(filtered_data['snp'], rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
