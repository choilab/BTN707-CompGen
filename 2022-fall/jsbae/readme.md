# JSBae
Insect microbiome analysis using MgnifyR

==================

Main purpose of this project is to make a thorough analysis of microbiome set between broad amount of insect samples in EBI. 
------------------
### 1. Mgnify database search / data gathering
   ####  1) Take a rough search thorugh the database, see which keyword would match the largest set of data.
   ##### * Insect / Insecta or specific nomenclature of organisms
   ####  2) Make a detailed search. Other parameters as biome, experiment type, sequencing method..etc
   ####  3) Decide qtype of search (samples, studies, analyses)
-----------
### 2. Data import & sorting
   ####  1) With some keywords for data import, data search & import can be held by query function via MgnifyR.
   ####  2) Sample data analyses & metadata can be imported by making an accession with analyes database.

-----------
### 3. Import as phyloseq data / further analysis
   ####  1) phyloseq-ize Data already in MgnifyR.
   ##### * Any data already in an R session can be annoated/coerced to be recognized by phyloseq’s functions and methods.
   ####  2) Set Tax_table, OTU_table for bar plot / phylogenetic tree construction, then import library(phyloseq)
   ####  3) Check the visualized data with variables, do the further analysis / data modification
   
  - Used language/Tool : R / MgnifyR
  - Target sample : Whole insect sample with 16S rRNA gene sequenced

-----------

Current workflow

 #### 1. Data search / Import from Database(Mgnify)
     -
 #### 2. Make a query function in MgnifyR environment
     -
 #### 3. Import data to phyloseq / Make a phylogenic classification of each OTUs from each sample
