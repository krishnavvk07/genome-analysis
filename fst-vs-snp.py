import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyexcel_ods

# Function to read .ods file and return DataFrame
def read_ods_to_dataframe(file_path):
    data = pyexcel_ods.get_data(file_path)
    sheet_data = data[list(data.keys())[0]]  # Assumes the first sheet
    df = pd.DataFrame(sheet_data[1:], columns=sheet_data[0])  # Assumes first row is header
    return df

# Load data from the provided ODS file
file_path = 'raw-spreadsheets/fst-vs-lon-pre-post.ods'
data = read_ods_to_dataframe(file_path)

# Filter out rows where Lon_pre is higher than Lon_post
filtered_data = data[
    data['lon_pre'] <= data['lon_post']
]

# Delete the row where SNP value is 'rs2681417'
filtered_data = filtered_data[filtered_data['snp'] != 'rs2681417']

# Define positions and width of bars
x = np.arange(len(filtered_data['snp']))  # the positions on the x-axis
width = 0.2  # Width of the bars on the plot

fig, ax = plt.subplots(figsize=(15, 8))

# Plot bars for each column
bars1 = ax.bar(x - width, filtered_data['lon_pre'], width, label='lon_pre', color='cornflowerblue')
bars2 = ax.bar(x, filtered_data['lon_post'], width, label='lon_post', color='brown')

# Labeling and layout
ax.set_xlabel('SNP')
ax.set_ylabel('FST')
ax.set_title('FST vs Time Period WRT Black Death')
ax.set_xticks(x)
ax.set_xticklabels(filtered_data['snp'], rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
