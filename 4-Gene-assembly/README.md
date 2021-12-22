# Students
서소월/황종현

## Gene Assembly Designer
* Input: gene/gene cluster/chromosome
* Output: a pool of variable lengths of oligos/fragments (overlapped) for synthetic full gene
* Options: ssDNA/dsDNA/overlap length/# of fragments/restriction site removal
* Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?...
* Example program & literature4 - Assmebly PCR oligo Maker

## Gene Assembly

![image](https://user-images.githubusercontent.com/82203595/146798776-bafd28ce-5034-4963-b5be-120ee5717463.png)

Fig.1 gene-assembly

![image](https://user-images.githubusercontent.com/82203595/146800227-f17cf6e9-b6d8-4c6b-a251-bfd3951df017.png)

Fig.2 types of gene assembly methods

- Restriction enzyme-based (BioBrick assembly, Golden Gate assembly)
- Sequence homology-based (Gibson assembly, SLIC, Overlap PCR, DNA assembler)
  - in vitro/in vivo
- Bridging oligo-based (LCR)

## Importance of gene-assembly
- Discover novel natrual product
- Design and characterize gene circuit
- Synthesize genomes
- Lower error rate
- Cost-effective

## Gene assembly design
![image](https://user-images.githubusercontent.com/82203595/146803889-71f0a18d-965f-436b-9990-f722a97ca695.png)

Fig.3 Algorithm of gene assembly design

## How to calculate Tm?
* considerable factors: length of oligonucleotide, GC content of oligonucleotide, concentration of oligonucleotide, salt environment including concentrations of monovalent(sodium, potassium), divalent(magnesium), polyvalent cations and dNTPs.

## Reference code of Primer Design for Gibson Assembly from Benchling
###Considered functions:
*  Tm of sequence
*  Reverse complement sequence
*  Measures the GC content of the sequence
*  Checkes the primer sequence for proper annealing
*   - Target melting temperature (usually >60 C and <80)
*   - GC content is within bound (usually >40% and <60%)
*   - 3 prime end contains a G or C
*  Checks GC content of a coding sequence
*  Picks the codon for an amino acid that matches the mask
*  Returns a coding DNA sequence for the amino acid sequence
*  Checks for repeats in the DNA sequence
*  Overlapping dna sequence for Gibson assemnbly
*  Annealing sequence (PCR region)
*  Primer design
*   - Step 1. Find restriction enzymes
*   - Step 2. Pick out 2 enzymes for cutting the 5' and 3' end 
*   - Step 3. Get overlap sequence for Gibson
*   - Step 4. Design annealing region for primer on the insert
*   - Step 5. Put together the primer
* https://github.com/alenkran/Benchling_Gibson_Primer_Design/commit/792419b8fabaf867c9caad06bcb0c7badf33d88d


## Benchmark
![benchmark](https://user-images.githubusercontent.com/82203595/146804483-3baad573-8adb-46f4-ba37-733387ac46f9.PNG)

Fig.4 Assemble input sequence with output fragments



## Reference code for testing Assembly Fragments
* https://github.com/BjornFJohansson/pydna/blob/6dd22c4a3708552220c2c52c712a23d951eca743/tests/test_module_design.py
---
## Reference
* [NEB Golden Gate Assembly Tool](https://goldengate.neb.com/)
