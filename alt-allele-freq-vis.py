import pandas as pd
import pyexcel_ods
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame()

# Function to read specific rows from an ODS file
def read_ods_from_header(file_path, sheet_name, header_row_index): 
    data = pyexcel_ods.get_data(file_path)
    sheet_data = data[sheet_name]  # Get data from the specified sheet

    # Extract header and data
    header = sheet_data[header_row_index]  # Header row
    data_rows = sheet_data[header_row_index + 1:]  # Data rows after the header
    
    # Convert to DataFrame
    df = pd.DataFrame(data_rows, columns=header)
    return df

file_path = 'dataset.ods'
sheet_name = 'S4'
header_row_index = 2  # 0-based index for the third header row

data = read_ods_from_header(file_path, sheet_name, header_row_index)

data.replace('', np.nan, inplace=True)
data.replace('NA', np.nan, inplace=True)

#Filter out cells with value 'NA'
data = data.dropna(subset=['Site'])

# Ensure the relevant columns are numeric for comparison
data[['London_Pre_Alt', 'London_During_Alt', 'London_Post_Alt']] = data[['London_Pre_Alt', 'London_During_Alt', 'London_Post_Alt']].apply(pd.to_numeric, errors='coerce')

# Remove rows where 'London_Pre_Alt' is higher than either 'London_During_Alt' or 'London_Post_Alt'
data = data[~((data['London_Pre_Alt'] > data['London_During_Alt']) | (data['London_Pre_Alt'] > data['London_Post_Alt']))]

# Define positions and width of bars
x = np.arange(len(data['Site']))  # the positions on the x-axis
width = 0.2  # Width of the bars on the plot

fig, ax = plt.subplots(figsize=(15, 8))

# Plot bars for each column
bars1 = ax.bar(x - width, data['London_Pre_Alt'], width, label='Allele Freq Pre-BD', color='cornflowerblue')
bars2 = ax.bar(x, data['London_During_Alt'], width, label='Allele Freq During-BD', color='brown')
bars3 = ax.bar(x + width, data['London_Post_Alt'], width, label='Allele Freq Post-BD', color='darkseagreen')

# Labeling and layout
ax.set_xlabel('Snp')
ax.set_ylabel('Allele Frequency')
ax.set_title('Plot of Alternate Allele Frequency vs Snp')
ax.set_xticks(x)
ax.set_xticklabels(data['Site'], rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
