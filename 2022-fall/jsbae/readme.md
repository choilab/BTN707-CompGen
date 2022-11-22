# JSBae
Insect microbiome analysis using MgnifyR / DADA2
==================

### Mgnify database search / data gathering
#### Take a rough search thorugh the database, see which keyword would match the largest set of data.
##### Insect / Insecta or specific nomenclature of organisms
#### Make a detailed search. Other parameters as biome, experiment type, sequencing method..etc
#### Decide qtype of search (samples, studies, analyses)
-----------
### Data import & sorting
#### With some keywords for data import, data search & import can be held by query function via MgnifyR.
#### sample data analyses & metadata can be imported by making an accession with analyes database.

-----------
### Import as phyloseq data / further analysis
#### phyloseq-ize Data already in MgnifyR.
##### Any data already in an R session can be annoated/coerced to be recognized by phyloseq’s functions and methods.
##### Set Tax_table, OTU_table for bar plot / phylogenetic tree construction, then import library(phyloseq)
