import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Adjust the path to where your test plot files are located
sys.path.insert(0, os.path.expanduser('~/repos/krishna-vadali-epedimiology-project/box-plot-code'))

# Import plot functions from other files
import gcsfnone as create_plot_1
import gcsfinfected as create_plot_2
import il1bnone as create_plot_3
import il1binfected as create_plot_4
import il10none as create_plot_5
import il10infected as create_plot_6
import ccl3none as create_plot_7
import ccl3infected as create_plot_8

fig, axs = plt.subplots(4, 2, figsize=(20, 20))

# Create each subplot
create_plot_1.create_plot(axs[0, 0])
create_plot_2.create_plot(axs[0, 1])
create_plot_3.create_plot(axs[1, 0])
create_plot_4.create_plot(axs[1, 1])
create_plot_5.create_plot(axs[2, 0])
create_plot_6.create_plot(axs[2, 1])
create_plot_7.create_plot(axs[3, 0])
create_plot_8.create_plot(axs[3, 1])

# Add common labels and titles
fig.text(0.5, 0.04, 'Genotypes', ha='center', va='center', fontsize=14)
fig.text(0.04, 0.5, 'Cytokine Value', ha='center', va='center', rotation='vertical', fontsize=14)

# Add individual row titles
axs[0, 0].set_title('No infection induced', fontsize=14)
axs[0, 1].set_title('Infection induced', fontsize=14)
axs[0, 0].annotate('G-CSF', xy=(0, 0.5), xytext=(-axs[0, 0].yaxis.labelpad - 5, 0), 
                   xycoords=axs[0, 0].yaxis.label, textcoords='offset points', 
                   size='large', ha='right', va='center')
axs[1, 0].annotate('IL1B', xy=(0, 0.5), xytext=(-axs[1, 0].yaxis.labelpad - 5, 0), 
                   xycoords=axs[1, 0].yaxis.label, textcoords='offset points', 
                   size='large', ha='right', va='center')
axs[2, 0].annotate('IL10', xy=(0, 0.5), xytext=(-axs[2, 0].yaxis.labelpad - 5, 0), 
                   xycoords=axs[2, 0].yaxis.label, textcoords='offset points', 
                   size='large', ha='right', va='center')
axs[3, 0].annotate('CCL3', xy=(0, 0.5), xytext=(-axs[3, 0].yaxis.labelpad - 5, 0), 
                   xycoords=axs[3, 0].yaxis.label, textcoords='offset points', 
                   size='large', ha='right', va='center')

# Define colors and labels for each genotype category
colors = ['blue', 'brown', 'darkolivegreen']
labels = ['Homozygous (deleterious allele)', 'Heterozygous', 'Homozygous (protective allele)']

# Create legend handles
handles = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]

# Add legend
fig.legend(handles=handles, loc='upper left', fontsize=9)

plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
plt.show()
