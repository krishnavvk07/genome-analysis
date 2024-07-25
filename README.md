# Genome analysis and interpretation project

Analyzing the effect of the single nucleotide polymorphism (SNP) rs2549782 of the ERAP2 gene in offering selective immunity over the Black Death while simultaneously increase susceptibility to autoimmune disorders. Epedemiological research project for the Institute for Computing in Research

## 1. Installing relevant libraries

Navigate to your home directory on the terminal `(home)$`

```
cd
``` 
 
### Installing pip:

In the home directory `$`

```
sudo apt install python3-pip
```

### Miniconda:

```mkdir -p ~/miniconda3```
```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh```
```~/miniconda3/miniconda.sh -b -u -p ~/miniconda3```
```rm -rf ~/miniconda3/miniconda.sh```

After installing, initialize Miniconda. The following commands initialize for bash or zsh shells:

Now, install the following packages:

`pip install biopython`
`conda install bioconda::mafft`
`pip install jupyterlab`

## Aligning sequences

Download the file `sequence_aligning.ipynb`. This jupyter notebook uses the MAFFT tool to provide a alignment of the sequences, while displaying previous and post-aligned lengths of sequences.

Running the command `jupyter notebook`. Then, the file `sequence_aligning.ipynb` can be selected.



