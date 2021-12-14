# Students
서소월/황종현

## Gene Assembly Designer
* Input: gene/gene cluster/chromosome
* Output: a pool of variable lengths of oligos/fragments (overlapped) for synthetic full gene
* Options: ssDNA/dsDNA/overlap length/# of fragments/restriction site removal
* Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?...
* Example program & literature4 - Assmebly PCR oligo Maker

## Gene Assembly
- Restriction enzyme-based (BioBrick assembly, Golden Gate assembly)
- Sequence homology-based (Gibson assembly, SLIC, Overlap PCR, DNA assembler)
  - in vitro/in vivo
- Bridging oligo-based (LCR)

## Gene assembly design
* Condiseration: overlap length of fragment/Tm/n of fragments/specificity of overlap

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

## Code for Gene Assembly
from Bio.Restriction import *
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import numpy as np
import os
import pandas as pd
import re
import requests
import json

COLOR = [255, 255, 0]
ignore_enzyme_list = ['AsuNHI']

my_seq = input ("DNA :")
        
seq=my_seq

### calculate Tm of overlapped sequence
def get_Tm(seq):
    """   Calculate melting temperature for DNA oligomer
    Melting tempearture is based on Primestar PCR Premix condition
   
    Args:
       seq: string of DNA sequence
    Returns:
       Tm: melting temperature (Celcius)
    """
    my_seq = Seq(seq)

print('%0.2f' % mt.Tm_NN(my_seq))

### check reverse sequence
def get_rc(seq):
    """   Returns the reverse complement sequence """
    return str(Seq(seq).reverse_complement())

rc = get_rc(my_seq)
print ("reverse complement :",rc)

### check GC content
def check_GC(seq):
    """   Measures the GC content of a sequence """
    return (seq.upper().count('G') + seq.upper().count('C'))/float(len(seq))

gc = check_GC(my_seq)
print ("GC content :",gc)

def check_codon(seq, GC_bound=[0.4, 0.6]):
    """ Checks GC content of a coding sequence
    Args:
        seq: string of DNA sequence
        GC_bound: boundary for acceptable GC content [low, high]
    Returns:
        Boolean for GC content check
    """

    GC_content = check_GC(seq)
    if GC_content < GC_bound[0] or GC_content > GC_bound[1]:
        return False
    return True

cc = check_codon(my_seq)
print("GC content of a coding sequence :",cc)

	### get fragments
	def get_fragments(seq):
	    """
    	get fragment sequence according to the number of fragments.
    	n is the number of fragments.
    	"""

	my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGGTGGCGATCGCCGAAGGAGTCCGCTCGAATCGGGCTCCTAGCTGATATTCGATCGATTGCCCCTAAGCTAGCTATCATCCCTAGCCTTAATATTCTCTCGCGCAGATCGATCGGGCAATATCGATCGGATCCGATCCGAAAGCCTAATCGAATCTCTAGAGCTAGCTAATTCGATCGATCTCCTAGAGCTCTAGCTAGCTTTGGGC")
	len(my_seq)

	n=4 #number of fragments

	#number_overlap = 25
	s=25
	n1=round(len(my_seq)/n)+s
	n2=round(len(my_seq)/n)*2+s
	n3=round(len(my_seq)/n)*3+s
    
	#get_fragment sequence
	for i in range(0,n1):
	    dna0 = my_seq[0:(i+s)]
	    dna1 = my_seq[i:(i+n1)]
    	dna2 = my_seq[(i+n1-s):(i+n2)]
    	dna3 = my_seq[(i+n2-s):(i+n3)]
    	dna4 = my_seq[(i+n3-s):(len(my_seq))]+dna0 

    	#get_overlapped sequence
    	dna1_2_overlap = my_seq[(i+n1-s):(i+n1)]
    	dna2_3_overlap = my_seq[(i+n2-s):(i+n2)]
    	dna3_4_overlap = my_seq[(i+n3-s):(i+n3)]
    	dna4_1_overlap = my_seq[i:(i+s)]
        
    seq=dna1_2_overlap
    if i == 0:
        if gc < 0.4 or gc > 0.6 and Tm > 60:
            i += 1
        else:
            print(dna1)
            print(seq)
    
    seq=dna2_3_overlap
    if i == 0:
        if gc < 0.4 or gc > 0.6 and Tm > 60:
            i += 1
        else:
            print(dna2)
            print(seq)
            
    seq=dna3_4_overlap
    if i == 0:
        if gc < 0.4 or gc > 0.6 and Tm > 60:
            i += 1
        else:
            print(dna3)
            print(seq)
            
    seq=dna4_1_overlap
    if i == 0:
        if gc < 0.4 or gc > 0.6 and Tm > 60:
            i += 1
        else:
            print(dna4)
            print(seq)
            

## 황종현 

	### Sequence Input
	my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGGTGGCGATCGCCGAAGGAGTCCGCTCGAATCGGGCTCCTAGCTGATATTCGATCGATTGCCCCTAAGCTAGCTATCATCCCTAGCCTTAATATTCTCTCGCGCAGATCGATCGGGCAATATCGATCGGATCCGATCCGAAAGCCTAATCGAATCTCTAGAGCTAGCTAATTCGATCGATCTCCTAGAGCTCTAGCTAGCTTTGGGC")
	print(len(my_seq))

	### Fragment Number Input
	n = int(input ("fragment 갯수 :"))

	### Overlap Length Input
	s = int(input ("overlap 길이 :"))

	### Overlap + DNA Fragment 서열 생성
	mod = sys.modules[__name__]
	
	for i in range(1,n+1):
	    if i < n:
	        a = round(len(my_seq)/n) * i + s
  	      globals()['df_{}'.format(i)] = a
    	if i == n:
      	  a = len(my_seq)
        	globals()['df_{}'.format(i)] = a
    	print(a)

	for x in range(0,n+1):
  	  if x == 0:
    	    globals()['dna_{}'.format(x)] = my_seq[0:s]
      	  print("DNA : ", getattr(mod, 'dna_{}'.format(x)))
    	if x == 1:
      	  globals()['dna_{}'.format(x)] = my_seq[0:(getattr(mod, 'df_{}'.format(x), x))]
        	print("DNA : ", getattr(mod, 'dna_{}'.format(x)))
    	if 1 < x < n: 
      	  b = my_seq[((getattr(mod, 'df_{}'.format(x-1), x)-s)):(getattr(mod, 'df_{}'.format(x), x))]
        	globals()['dna_{}'.format(x)] = b
        	print("DNA : ", getattr(mod, 'dna_{}'.format(x)))
	    if x == n:
  	      bb = my_seq[((getattr(mod, 'df_{}'.format(x), x))-s):(len(my_seq))] + dna_0
    	    globals()['dna_{}'.format(x)] = bb
      	  print("DNA : ", getattr(mod, 'dna_{}'.format(x)))


## Reference code for testing Assembly Fragments
* https://github.com/BjornFJohansson/pydna/blob/6dd22c4a3708552220c2c52c712a23d951eca743/tests/test_module_design.py
---
## Reference
* [NEB Golden Gate Assembly Tool](https://goldengate.neb.com/)
