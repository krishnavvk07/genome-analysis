#!/usr/bin/env python
# coding: utf-8


from Bio import SeqIO
import subprocess
from io import StringIO


fasta = list(SeqIO.parse('/home/krishna/repos/krishna-vadali-epedimiology-project/erap2_gene.fna', format = 'fasta'))

command = ['mafft', 'erap2_gene.fna']

# Open the output file
with open('erap2_gene_aligned.fasta', 'w') as output_file:
    # Run the command and redirect the output to the file
    subprocess.run(command, stdout=output_file, check=True)

print("Alignment completed and saved to erap2_gene_aligned.fasta")



