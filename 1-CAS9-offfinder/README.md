# Project Description 
* Nisha
* 이현주

---
## Project - Prediction of On/Off Targets & gRNA designer for CRISPR Genome Editing

### Usage example:
- Input: genome sequence/target gene/oligo (.fna/.fasta nucleotide)
- Output: target/off-target site (.coordinate)
- Options: # of mismatches/positional mismatches/insertion/deletion/base ambiguity
- Example program & literature[^offfinder] - [CAS-off-finder http://www.rgenome.net/cas-offinder/](http://www.rgenome.net/cas-offinder/)
   [^offfinder]:[Cas-OFFinder: a fast and versatile algorithm that searches for potential off-target sites of Cas9 RNA-guided endonucleases](https://academic.oup.com/bioinformatics/article/30/10/1473/267560)

### Contents
#### i) what is the problem to solve? 
- CRISPR Cas OFFinder put input of PAM site, target genome, query sequence and get how many off target in target genome based on query sequence and PAM site.
- It should have all information of target genome, query sequence and PAM site.
- So we decide our program put only target genome and query sequence and compare all PAM DB to find what PAM system is the most matched and least off-target.
#### ii) why is it important? (biological meaning) 
- It will get whole off target about one target genome based on PAM site.
- It's convenient that doesn't have to compare all PAM system and get most profit PAM system.
#### iii) how can we design/build/test?
- It will be shown below that how to design, build, test our project.


---
### Design of guide RNA and Off-target effect in CRISPR Genome Editing
With discovery of microbial CRISPR-CAS systems, now any genome can be editied by RNA-guided DNA endonuclease from the modified CRISPR system. This genome editing requires guide RNA for targeting specific genomic locus. When we design the guide RNA, a few rules can be applied. Although CRISPR systems are very efficient genome editing tools, off-target editing can be made at very low rate. For gene therapeutic usage, we should design a gude RNA for specific target in genome and evaluate the designed guide RNA by its off-target possibility. 

---
### Following is CAS-off-finder

[Fig. 1 Algorithmic flow of the CAS-off-finder program](https://user-images.githubusercontent.com/79410957/139711521-9a00c6ef-0f09-4256-9dfb-ffc57cbbcd53.png)
- Figure-1-(A) means the scheme of Cas-OFFinder. It finds 20bp of matched query sequence and 3bp of PAM site in SpCas9.
- Figure-1-(B) means the workflow algorithm of Cas-OFFinder. It has three wrappers and kenel(searching, comparing) is between the wrappers.
- Figure-1-(C) is running time per target site as a function of the number of input target sites via CPU (black squares) and GPU (red circles).

---
### coursera "string" practical course
- we may use string to read genome in python
- what process needs?
1. get input file(FASTA format)
2. parse FASTA with one long read
3. choose one Cas sequence from Cas sequences storage
4. compare by moving one base at a time
5. print matched sequence & after some of bases that are predicted as PAM site.
6. if PAM site is matched, it will be on-target.
7. if PAM site is not matched, it will be off-target.


---
### Focus Flow of project

- we focus on how to use Cas OFFinder's off-target finding tool
- off-target has meaning ? -> Is it meaningful ? -> Let's find readings which contain both "off-target" & "function"

<img width="451" alt="short algorithm" src="https://user-images.githubusercontent.com/79410957/144918085-91f97f63-2d3e-4bfa-928f-d6c3d0a606d3.png">

---
- we first think about sample sequence as Mycoplasma because of small size.
- however, after find some other software, we decided not to focus on specific genome. It will be used on any kind of genomes which is FASTA.

- we have to find some meaning of off-target -> maybe interview C.H. Jung Prof.'s lab
   
- we found CRISPR gDNA software(from Genious) which can find whole information about input gDNA.
- so, we thought our project is combining Genious and OFFinder called "How is suit gDNA to CRISPR"
- we made more detailed project flow.


<img width="451" alt="result progress" src="https://user-images.githubusercontent.com/79410957/144918212-ae65b8e1-ca36-4f76-999b-b430df6a4305.png">
---

After final presentation, 

- genome, gene -> gene knockout editing oligo set
- PAM -> find gRNA -> optimal (off target X, PAM distance mismatch) -> score

-from Geneious prime [Score system about activity of CRISPR site](https://www.geneious.com/tutorials/finding-crispr-sites-r9/) 


"By default Geneious Prime will use the method of Doench et al. (2016) to score the activity of the CRISPR sites. Activity, or on-target scoring, models the sequence features of the gRNA site itself to predict activity. When you run the Doench et al. (2016) model for the first time, Geneious will install the required dependencies (python and R) prior to running the model so you may notice it take a little longer."

---
- Find target with PAM site
- assume crRNA = "CAGCAACTCCAGGGGGCCGC" or "AAAGGAAACCATTGTGTTAA"(from CAS-OFFinder)
- Find matched sequence with start site(this will be on target)
- Find similar tool named [CRISPOR](http://crispor.tefor.net/crispor.py?batchId=3TeBYMvGLsICUasefwi6)
- Tried Homo sapiens (hg19), chr7:5569177-5569415, reverse genomic strand with N(20)NGG : PAM site.
- More detail of result is in [CRISPOR-result](https://github.com/choilab/BTN707-2021-Fall/blob/main/1-CAS9-offfinder/CRSIPOR-result-guides_hg19-chr7-5569176-5569415.xls)

![image](https://user-images.githubusercontent.com/79410957/146033455-c61df314-6ecd-4399-b9ea-2cdce03cae41.png)
- It showed whole result we want which is Guide Sequence + PAM and four types of specificity socring algorithms.
![image](https://user-images.githubusercontent.com/79410957/146033856-ccc17a6f-e74f-4def-921c-1e5811cb38ae.png)

---
#### CRISPOR has four scoring algorithms shown below.
##### MIT Specificity Score 
- The higher the specificity score, the lower are off-target effects in the genome.
- The specificity score ranges from 0-100 and measures the uniqueness of a guide in the genome. See [Hsu et al. Nat Biotech 2013](https://www.nature.com/articles/nbt.2647). We recommend values >50, where possible. See the [CRISPOR manual](http://crispor.tefor.net/manual/#offs)

##### CFD spec. Score
- The CFD specificity score, inspired like guidescan.com, behaves like the MIT specificity score, but it is based on the more accurate CFD off-target model, from [Doench 2016](https://www.nature.com/articles/nbt.3437), which is also used by Crispor to rank the off-targets. The CFD specificity score correlates better than the MIT score with the total off-target cleavage fraction of a guide, see [Tycko et al, Nat Comm 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6731277/) and also the [CRISPOR manual](http://crispor.tefor.net/manual/#faq).

##### Predicted Efficiency - Doench 16
- Aka the 'Fusi-Score', since V4.4 using the version 'Azimuth', scores are slightly different than before April 2018 but very similar (click 'show all' to see the old scores). Range: 0-100. Boosted Regression Tree model, trained on data produced by Doench et al (881 guides, MOLM13/NB4/TF1 cells + unpublished additional data). Delivery: lentivirus. See [Fusi et al. 2015](https://www.biorxiv.org/content/10.1101/021568v1) and [Doench et al](https://www.nature.com/articles/nbt.3437). 2016 and crispr.ml. Recommended for guides expressed in cells (U6 promoter). Click to sort the table by this score.

##### Predicted Efficiency - Mor Mateos
- Also called 'CrisprScan'. Range: mostly 0-100. Linear regression model, trained on data from 1000 guides on >100 genes, from zebrafish 1-cell stage embryos injected with mRNA. See [Moreno-Mateos et al.](https://www.nature.com/articles/nmeth.3543). Recommended for guides transcribed in-vitro (T7 promoter). Click to sort by this score. Note that under 'Show all scores', you can find a Doench2016 model trained on Zebrafish scores, Azimuth in-vitro, which should be slightly better than this model for zebrafish.

