import sys
import os
import pandas as pd
import pyexcel_ods
import matplotlib.pyplot as plt
import numpy as np

# Function to read specific rows from an ODS file
def read_ods_from_header(file_path, sheet_name, header_row_index):
    data = pyexcel_ods.get_data(file_path)
    sheet_data = data.get(sheet_name)
    
    # Extract header and data
    header = sheet_data[header_row_index]  # Header row
    data_rows = sheet_data[header_row_index + 1:]  # Data rows after the header
    
    # Convert to DataFrame
    df = pd.DataFrame(data_rows, columns=header)
    return df

def create_plot(ax):
    file_path = 'boxplot.ods'
    sheet_name = 'S84I'
    header_row_index = 1  # 0-based index for the second header row

    data = read_ods_from_header(file_path, sheet_name, header_row_index)

    # Create a DataFrame for the box plot
    box_data = pd.DataFrame({
        'T/T': data['T/T'],
        'T/C': data['T/C'],
        'C/C': data['C/C']
    })

    # Define colors and labels for each genotype category
    colors = ['blue', 'brown', 'darkolivegreen']
    labels = ['Homozygous(protective allele)', 'Heterozygous', 'Homozygous(deleterious allele)']

    # Create the box plot using matplotlib
    # Use the provided axis
    boxplot = ax.boxplot(
        [box_data[col].dropna() for col in box_data.columns],
        labels=box_data.columns,
        patch_artist=True,
    )

    # Customize colors for each box
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

# This block will be removed when importing into a larger script
if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(8, 6))
    create_plot(ax)
    plt.show()
