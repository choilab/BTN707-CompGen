# Team
* Nisha/이현주

---

1. CRISPR Genome Editing - Prediction of On/Off Target & gRNA designer

   - Input: genome sequence/target gene/oligo (.fna/.fasta nucleotide)
   - Output: target/off-target site (.coordinate)


   - Options: # of mismatches/positional mismatches/insertion/deletion/base ambiguity


   - Thinkabouts: 
i) what is the problem to solve?, 

ii) why is it important? (biological meaning), 

iii) how can you design/build/test?... 


   - Example program & literature[^offfinder] - [CAS-off-finder http://www.rgenome.net/cas-offinder/](http://www.rgenome.net/cas-offinder/)
   [^offfinder]:[Cas-OFFinder: a fast and versatile algorithm that searches for potential off-target sites of Cas9 RNA-guided endonucleases](https://academic.oup.com/bioinformatics/article/30/10/1473/267560)

---

hyunju's memo that introduction will include
- what CRISPR is
- what we want to do by coding CAS off finder
- how existing CAS off finder works

As I write it, it is similar to Thinkabouts,,,

---

Divide parts to explaining basic concept and telling CAS-off-finder.


We should include our direction(what we are going to do refer to CAS-off-finder).

---

![CAS-off-finder](https://user-images.githubusercontent.com/79410957/139711521-9a00c6ef-0f09-4256-9dfb-ffc57cbbcd53.png)
- (A) The scheme of Cas-OFFinder. 
- (B) The workflow of Cas-OFFinder. 
- (C) Running time per target site as a function of the number of input target sites via CPU (black squares) and GPU (red circles)

---
until this week,
- we will make list of Cas system
- we chose 30 types of Cas system
- record in table format to read well

table | a
----- | ---
1     | 2

---
coursera "string" practical course
- we may use string to read genome in python
https://www.coursera.org/learn/dna-sequencing/lecture/QQsZP/practical-string-basics

---
