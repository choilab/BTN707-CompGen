Structurally similar protein finder
======================================

<br/><br/>

## Brief description

This pipeline finds most similar protein structures using foldseek program. You can upload protein structure file as PDB format. Sspf query uploaded structure in [Alphafold DB](https://alphafold.ebi.ac.uk/). Options to select DB by species, to query using PDB ID instead of PDB file are developing.

<br/>

## Requirements for local install

#### System requirement

Linux(Ubuntu) is recommanded. You can install require programs on Mac, therefore, this pipeline is developed on Ubuntu.

<br/>

#### Program requirement

[foldseek](https://github.com/steineggerlab/foldseek/blob/master/README.md) and [Django](https://www.djangoproject.com/) programs are used in this pipeline. Django transfers uploaded PDB file to server, and foldseek query similar structures.

|Program|version|system requirement|description|
|---|---|---|---|
|foldseek|3.915ef7d|Linux, Mac||
|Django|4.1.3|Linux, Mac, Windows||

<br/>

#### Program installation





<br/><br/>

