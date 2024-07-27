import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyexcel_ods

# Function to read .ods file and return DataFrame
def read_ods_to_dataframe(filtered_altered_allele):
    data = pyexcel_ods.get_data(filtered_altered_allele)
    sheet_data = data[list(data.keys())[0]]  # Assumes the first sheet
    df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])  # Assumes first row is header
    return df

# Load data from an ODS file
data = read_ods_to_dataframe('filtered_altered_allele.ods')

# Define positions and width of bars
x = np.arange(len(data['site']))  # the positions on the x-axis
width = 0.2 # Width of the bars on the plot

fig, ax = plt.subplots()

# Plot bars for each column
bars1 = ax.bar(x - width, data['Lon_pre'], width, label='Lon_pre', color='blue')
bars2 = ax.bar(x, data['Lon_dur'], width, label='Lon_dur', color='red')

# Labeling and layout
ax.set_xlabel('SNPs')
ax.set_ylabel('Allele frequency')
ax.set_title('Plot of alternate allele frequency vs SNP')
ax.set_xticks(x)
ax.set_xticklabels(data['site'])
ax.set_xticklabels(data['site'], rotation=45, ha='right')
ax.legend()

plt.show()
