Structurally similar protein finder
======================================

<br/><br/>

## Brief description

You can upload protein structure file as PDB format. Sspf query uploaded structure in [Alphafold DB](https://alphafold.ebi.ac.uk/) using [foldseek](https://github.com/steineggerlab/foldseek). Options to select DB by species, to query using PDB ID instead of PDB file are developing.

<br/>

## Purpose of program

#### Importance of protein structure

Protein is most important functional polymer in living organisms. Determining function of protein is one of main goal of modern biology. Protein contains not only sequencial information like DNA/RNA, but also structural information. Chemical properties are determined by structure and functions are determined by chemical properties. 


#### One step querying

![output](https://user-images.githubusercontent.com/104611489/208581150-3f4d9fd2-9abf-4490-bd4a-a24fc5300b25.png)



Alphafold predicted protein structures of genes in Uniprot DB. Protein structures of protein coading genes in 16 model organisms and 32 global health proteomes predicted by alphafold are provided on [Alphafold-EBI database](https://alphafold.ebi.ac.uk/download). Many protein structure comparing tools exist, however, downloading structure data, running program and 3D visualization of output protein is time consuming steps. This pipeline cut down these steps to one step. 

<br/><br/>

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
    # django-admin startproject sspf
 
Then, clone sourcecode file on your project, go to your project folder which contains manage.py. and do
 
    # python manage.py makemigration
    # python manage.py migrate



<br/><br/>





