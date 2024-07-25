# Genome analysis and interpretation project

Analyzing the effect of the single nucleotide polymorphism (SNP) rs2549782 of the ERAP2 gene in offering selective immunity over the Black Death while simultaneously increase susceptibility to autoimmune disorders. Epedemiological research project for the Institute for Computing in Research

## 1. Installing relevant libraries

Navigate to your home directory on the terminal `(home)~$`

```
cd
``` 

Next,

```
sudo apt install python3-pip
```

## 2. Installing MAFFT (Multiple alignment program)	

### Download link:

```
[mafft-7.526-linux.tgz](https://mafft.cbrc.jp/alignment/software/mafft-7.526-linux.tgz) (64-bit only)
```

### Installation:

1. Open a Terminal window.
2. Untar the `.tgz` file in any folder you like.
```
$ cd /somewhere/
$ tar xfvz mafft-7.526-linux.tgz
```
The `mafft-linux64` folder is generated, which has the `mafft.ba` script and the `mafftdir` subfolder.

```

$ cd /somewhere/
$ ls -F
mafft-linux64/
$ cd mafft-linux64/
$ ls -F
mafft.bat*       mafftdir/
```
If you want to move the installation to another location, just move the entire `mafft-linux64` folder (that contains both `mafft.bat` and `mafftdir`) to the new location. 


Now, install the following packages:

`pip install biopython`
`conda install bioconda::mafft`
`pip install jupyterlab`

## Aligning sequences

Download the file `sequence_aligning.ipynb`. This jupyter notebook uses the MAFFT tool to provide a alignment of the sequences, while displaying previous and post-aligned lengths of sequences.

Running the command `jupyter notebook`. Then, the file `sequence_aligning.ipynb` can be selected.



