Structurally similar protein finder
======================================

<br/><br/>

## Brief description

This pipeline finds most similar protein structures using foldseek program. You can upload protein structure file as PDB format. Sspf query uploaded structure in [Alphafold DB](https://alphafold.ebi.ac.uk/). Options to select DB by species, to query using PDB ID instead of PDB file are developing.

<br/>

## Purpose of program



##### functions of protein (reference : http<hi>s://alevelbiolo<hi>gy.co.uk/notes/functions-of-proteins/)

Protein is most important functional polymer in living organisms. Determining function of protein is main goal of modern biology. Protein contains not only sequencial information like DNA/RNA, but also structural information. Chemical properties are determined by structure and functions are determined by chemical properties. 

Alphafold predicted protein structures of known protein coading genes in Uniprot DB. Protein structures of protein coading genes in 16 model organisms and 32 global health proteomes predicted by alphafold are provided on [Alphafold-EBI database](https://alphafold.ebi.ac.uk/download). Many protein structure comparing tools exist, however, downloading structure data, running program and 3D viewing output protein is time consuming steps. This pipeline cut down these steps to one step. 



## Requirements for local install


#### Program requirement

[foldseek](https://github.com/steineggerlab/foldseek/blob/master/README.md) and [Django](https://www.djangoproject.com/) programs are used in this pipeline. Django transfers uploaded PDB file to server, and foldseek query similar structures. For system requirement, linux(Ubuntu) is recommanded. You can install require programs on Mac, therefore, this pipeline is developed on Ubuntu.

|Program|version|system requirement|description|
|---|---|---|---|
|foldseek|3.915ef7d|Linux, Mac||
|Django|4.1.3|Linux, Mac, Windows||
|Molstar||Web|only web pipeline, not local|
    
<br/>

#### Program installation

    # conda install foldseek
    # conda install django
    # django-admin startproject (your project name)
 
Then, clone sourcecode file on your project, go to your project folder which contains manage.py. and do
 
    # python manage.py makemigration
    # python manage.py migrate



<br/><br/>

