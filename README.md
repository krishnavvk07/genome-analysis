# Genome analysis and interpretation project

Analyzing the effect of the single nucleotide polymorphism (SNP) rs2549782 of the ERAP2 gene in offering selective immunity over the Black Death while simultaneously increasing susceptibility to autoimmune disorders. Epedemiological research project for the Institute for Computing in Research

## 1. Installing relevant libraries

Navigate to your home directory on the terminal `(home)~$`

```bash
cd
``` 

Next,

```bash
sudo apt install python3-pip
sudo apt install pip
pip install biopython
pip install notebook
```

## 2. Installing MAFFT (Multiple alignment program)	

### Download Mafft from their official website: [MAFFT](https://mafft.cbrc.jp/alignment/software/mafft-7.526-linux.tgz)(64-bit only)

The file should be named `mafft-7.526-linux.tgz`.

### Moving the file to home directory:

1. Open a terminal window and navigate to your home directory. Then,

```bash
mv /directory_containing_downloads/mafft-7.526-linux.tgz .
```

### Installation:

1. Open a Terminal window.
2. Untar the `.tgz` file to your home directory.
```bash
cd
tar xfvz mafft-7.526-linux.tgz
```
The `mafft-linux64` folder is generated, which has the `mafft.ba` script and the `mafftdir` subfolder.

```bash
cd mafft-linux64/
ls -F
mafft.bat*       mafftdir/
```
If you want to move the installation to another location, just move the entire `mafft-linux64` folder (that contains both `mafft.bat` and `mafftdir`) to the new location. 

## Cloning repository

Clone the repository to be able to access all relevant files and run the program without further tweaks.

In the home directory,

```bash
mkdir repos
cd repos
git init
git clone https://codeberg.org/krishnavvk/krishna-vadali-epidemiology-project.git
```

## Aligning sequences:

The MAFFT tool allows us to align genomic data of nucleotides and amino acid sequences. We will use it to align the ERAP2 gene's output.

### Usage (through Jupyter notebook)

```bash
cd
jupyter notebook sequence_aligning.ipynb
```

Follow instructions on the Jupyter notebook to align the erap2 genome sequence and create an outpute file with the aligned sequence.







