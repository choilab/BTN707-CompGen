Structurally similar protein finder
======================================

<br/><br/>

## Brief description

This pipeline finds most similar protein structures using foldseek program. You can upload protein structure file as PDB format. Sspf query uploaded structure in [Alphafold DB](https://alphafold.ebi.ac.uk/). Options to select DB by species, to query using PDB ID instead of PDB file are developing.

<br/>

## Purpose of program


##### https://alevelbiolo<hi>gy.co.uk/notes/functions-of-proteins/

Protein is most important functional polymer in living organisms. function of proteins is determined by structure. 

Alphafold predicted protein structures of known protein coading genes in Uniprot DB. Protein structures of protein coading genes in 16 model organisms and 32 global health proteomes predicted by alphafold are provided on [Alphafold-EBI database](https://alphafold.ebi.ac.uk/download). 



## Requirements for local install


#### Program requirement

[foldseek](https://github.com/steineggerlab/foldseek/blob/master/README.md) and [Django](https://www.djangoproject.com/) programs are used in this pipeline. Django transfers uploaded PDB file to server, and foldseek query similar structures. For system requirement, linux(Ubuntu) is recommanded. You can install require programs on Mac, therefore, this pipeline is developed on Ubuntu.

|Program|version|system requirement|description|
|---|---|---|---|
|foldseek|3.915ef7d|Linux, Mac||
|Django|4.1.3|Linux, Mac, Windows||

<br/>

#### Program installation

    # conda install foldseek
    # conda install django
    # django-admin startproject (your project name)
 
Then, clone sourcecode file on your project, go to your project folder which contains manage.py. and do
 
    # python manage.py makemigration
    # python manage.py migrate



<br/><br/>

