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
     - 380 analysis datas retrieved from Mgnify database, make a data repository in User PC.
 #### 2. Make a query function in MgnifyR environment / sample information & metadata overall summary
     - Define it to Insect microbiome 16S rRNA amplicon data, also retrieve metadata of each sample.
 #### 3. Import data to phyloseq / Make a phylogenic classification of each sample.
     - OTU based-analysis / Making an microbiome community analysis of whole sample bulk.
 #### 4. Visualizing data with multi-aspects of metadata parameters.
     - Showing Bar plot / Plot ordination / Plot tree / Plot heatmap with diverse parameters to make a comparision between samples
 
 
 
 <img width="612" alt="image" src="https://user-images.githubusercontent.com/113403504/207232060-572b8160-f673-49a8-ab87-8bf4c4da8de0.png">
 
 ##### 1. Bar plot figure showing microbiome community of insecta amplicon samples(380ea) in Phylum level.

<img width="915" alt="image" src="https://user-images.githubusercontent.com/113403504/207233734-7eea138f-f1c8-465f-b591-5bfe998a4ba1.png">

 ##### 2. Bar plot figure showing microbiome community of insecta amplicon samples(380ea) in Class level.
 
 <img width="920" alt="image" src="https://user-images.githubusercontent.com/113403504/207234640-15a7f0f8-354f-4ad4-926e-74e5a4151b3e.png">

 ##### 3. Bar plot figure showing microbiome community of insecta amplicon samples(380ea) in Family level.
 
  <img width="915" alt="image" src="https://user-images.githubusercontent.com/113403504/207234355-2df28d22-159f-4cde-b88c-191f57eb7cb9.png">
 
 ##### 4. Bar plot figure showing microbiome community of insecta amplicon samples(380ea) in Order level.
 
 <img width="921" alt="image" src="https://user-images.githubusercontent.com/113403504/207235814-a42c772c-282d-4098-9286-246a63e97669.png">

##### 5. Bar plot figure showing microbiome community of insecta amplicon samples(380ea) in Genus level.

<img width="697" alt="image" src="https://user-images.githubusercontent.com/113403504/207236484-3fb6c92e-b9f1-49d6-9f4c-f7f58a0cfd7b.png">

##### 1) Plot organization showing sample collected longitude 

<img width="697" alt="image" src="https://user-images.githubusercontent.com/113403504/207237220-b6decca3-7a4e-42c0-86ef-ace9e9a35436.png">

##### 2) Plot organization showing sample collected latitude 


#### * Goal for next week

##### 1) Make readable visualization in case of plot bar
##### 2) Draw plot phylogenetic tree with obtained OTUs of samples 
##### 3) Make visualization which shows comparision between sample with different parameters of metadata

----------------------------------------------------------------------------------------------------------

<img width="667" alt="Screen Shot 2022-12-20 at 4 24 24 PM" src="https://user-images.githubusercontent.com/113403504/208607933-a1285169-c99e-4ec7-a86d-a97e83c718f9.png">

<img width="671" alt="Screen Shot 2022-12-20 at 4 24 43 PM" src="https://user-images.githubusercontent.com/113403504/208607974-464cd7c4-8838-4c80-bc04-13eb1a8f0504.png">

##### Output creation using R markdown

## Remaining procedure

### 1. Usable options of sample metadata for analysis between samples are not enough
### 2. Limit of analysis scope due to low diversity of host species
### 3. Detailed analysis of result should be done
### 4. Phylogenetic tree construction should be done
### 5. Output using R markdown should be done





