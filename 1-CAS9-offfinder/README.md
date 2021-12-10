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
- what process needs?
1. get input file(FASTA format)
2. parse FASTA with one long read
3. choose one Cas sequence from Cas sequences storage
4. compare by moving one base at a time
5. print matched sequence & after some of bases that are predicted as PAM site.
6. if PAM site is matched, it will be on-target.
7. if PAM site is not matched, it will be off-target.
8.  

---
until next week,
- we focus on how to use Cas OFFinder's off-target finding tool
- off-target has meaning ? -> Is it meaningful ? -> Let's find readings which contain both "off-target" & "function"

---
after 11/04 meet up,
- we decided to focus on Mycoplasma-specific Cas system Finder
- Why Mycoplasma? -> the smallest genome in the world
- we have to find some meaning of off-target -> maybe interview C.H. Jung Prof.'s lab
---

after 11/22 meet up,
- we decided not to focus on specific genome. It will be used on any kind of genomes which is FASTA.
- we should include OFF target story on presentation.
- we found CRISPR gDNA software(from Genious) which can find whole information about input gDNA.
- so, we thought our project is combining Genious and OFFinder called "How is suit gDNA to CRISPR"
- we made more detailed project flow.

24 Nov. presentation 
- What is CAS OFFinder 
- How it works
- What are the advantages 
- Analysis of the results from two different software i.e. Geneious prime and CRISPR RGEN tools


---
After final presentation, 

- genome, gene -> gene knockout editing oligo set
- PAM -> find gRNA -> optimal (off target X, PAM distance mismatch) -> score

-from Geneious prime [Score system about activity of CRISPR site](https://www.geneious.com/tutorials/finding-crispr-sites-r9/) 


"By default Geneious Prime will use the method of Doench et al. (2016) to score the activity of the CRISPR sites. Activity, or on-target scoring, models the sequence features of the gRNA site itself to predict activity. When you run the Doench et al. (2016) model for the first time, Geneious will install the required dependencies (python and R) prior to running the model so you may notice it take a little longer.
