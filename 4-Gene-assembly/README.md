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
        
    	if i == 0:
       	    seq = dna1_2_overlap
     	    tm1 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        	    print(tm1)
        	    gc1 = check_GC(seq)
                print ("gc1 :",gc1)
        
        	    seq = dna2_3_overlap
        	    tm2 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        	    print(tm2)
        	    gc2 = check_GC(seq)
        	    print ("gc2 :",gc2)
        
        	    seq = dna3_4_overlap
        	    tm3 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        	    print(tm3)
        	    gc3 = check_GC(seq)
        	    print ("gc3 :",gc3)
    
        	    seq = dna4_1_overlap
        	    tm4 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        	    print(tm4)
        	    gc4 = check_GC(seq)
        	    print ("gc4 :",gc4)
        
        	    while max([tm1,tm2,tm3,tm4]) > 60 or min([gc1,gc2,gc3,gc4]) < 0.4 or max([gc1,gc2,gc3,gc4]) > 0.6:
            		dna1 = my_seq[i:(i+n1)]
            		dna1_2_overlap = my_seq[(i+n1-s):(i+n1)]
            		seq = dna1_2_overlap
            		tm1 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
            		gc1 = check_GC(seq)
            		dna2 = my_seq[(i+n1-s):(i+n2)]
            		dna2_3_overlap = my_seq[(i+n2-s):(i+n2)]
            		seq = dna2_3_overlap
            		tm2 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
            		gc2 = check_GC(seq)
            		dna3 = my_seq[(i+n2-s):(i+n3)]
            		dna3_4_overlap = my_seq[(i+n3-s):(i+n3)]
            		seq = dna3_4_overlap
            		tm3 = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
            		gc3 = check_GC(seq)
            		dna0 = my_seq[0:(i+s)]
            		dna4 = my_seq[(i+n3-s):(len(my_seq))]+dna0
            		dna4_1_overlap = my_seq[i:(i+s)]
            		seq = dna4_1_overlap
            		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
            		gc4 = check_GC(seq)
           			i += 1

                    else:
            		print(i)
            		print(tm1)
            		print(gc1)
            		print("dna1:",dna1)
            		print("dna1_2_overlap:",dna1_2_overlap)
            		print(tm2)
            		print(gc2)
            		print("dna2:",dna2)
            		print("dna2_3_overlap:",dna2_3_overlap)
            		print(tm3)
            		print(gc3)
            		print("dna3:",dna3)
            		print("dna3_4_overlap:",dna3_4_overlap)
            		print(tm4)
           			print(gc4)
            		print("dna4:",dna4)
            		print("dna4_1_overlap:",dna4_1_overlap)
            		break
	
	### get assembled gene and compare with target input
    gene = dna1[0:-s] + dna2[0:-s] + dna3[0:-s] + dna4[0:-s]
    seq = my_seq[i-1:]+my_seq[0:i-1]
    gene == seq
	
	### get primer sequence
	def primer_sequence(seq):
        """ primer sequence for each frament """
         
	s = 22

	for x in range(0, n0-s):
    		primer1_F = dna4_1_overlap + dna1[s:s+x]
    		seq = primer1_F
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
    		x = 0
    		while tm < 60:
        		primer1_F = dna4_1_overlap + dna1[s:s+x]
        		seq = primer1_F
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		x += 1
    		else:
        		print("primer1_F:",primer1_F)
        		print(x)
        		print(tm)
        		break
        

	for x in range(0, n0-s):
    		primer2_F = dna1_2_overlap + dna2[s:s+x]
    		seq = primer2_F
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
    		x = 0
    		while tm < 60:
        		primer2_F = dna1_2_overlap + dna2[s:s+x]
        		seq = primer2_F
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		x += 1
   		else:
        		print("primer2_F:",primer2_F)
        		print(x)
        		print(tm)
        		break
                
        
	for x in range(0, n0-s):
    		primer3_F = dna2_3_overlap + dna3[s:s+x]
    		seq = primer3_F
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
    		x = 0
    		while tm < 60:
        		primer3_F = dna2_3_overlap + dna3[s:s+x]
        		seq = primer3_F
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		x += 1
    		else:
        		print("primer3_F:",primer3_F)
        		print(x)
        		print(tm)
        		break


	for x in range(0, n0-s):
    		primer4_F = dna3_4_overlap + dna4[s:s+x]
    		seq = primer4_F
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
    		x = 0
    		while tm < 60:
        		primer4_F = dna3_4_overlap + dna4[s:s+x]
        		seq = primer4_F
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		x += 1
    		else:
        		print("primer4_F:",primer4_F)
        		print(x)
        		print(tm)
        		break 
	
	### check reverse sequence
	def get_rc(seq):
    	"""   Returns the reverse complement sequence """
    		return str(Seq(seq).reverse_complement())
	seq = primer3_F
	rc = get_rc(seq)
	print ("reverse complement :",rc)
	
	# get reverse primer sequence
	def get_primer_R(seq):
    	""" get reverse primer sequence for each fragment """

	for y in range (0,n0-s):
    		R1 = dna1[-s-y:-s] + dna1_2_overlap
   		seq = R1
    		primer1_R = get_rc(seq)
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
   
    		y = 0
    		while tm < 60:
        		R1 = dna1[-s-y:-s] + dna1_2_overlap
        		seq = R1
        		primer1_R = get_rc(seq)
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		y += 1
    		else:
        		print("primer1_R:",primer1_R)
        		print(y)
        		print(tm)
        		break

	for y in range (0,n0-s):
    		R2 = dna2[-s-y:-s] + dna2_3_overlap
    		seq = R2
    		primer2_R = get_rc(seq)
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
   
    		y = 0
    		while tm < 60:
        		R2 = dna2[-s-y:-s] + dna2_3_overlap
        		seq = R2
        		primer2_R = get_rc(seq)
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		y += 1
    		else:
        		print("primer2_R:",primer2_R)
        		print(y)
        		print(tm)
        		break

	for y in range (0,n0-s):
    		R3 = dna3[-s-y:-s] + dna3_4_overlap
    		seq = R3
    		primer3_R = get_rc(seq)
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
   
    		y = 0
    		while tm < 60:
        		R3 = dna3[-s-y:-s] + dna3_4_overlap
        		seq = R3
        		primer3_R = get_rc(seq)
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		y += 1
    		else:
        		print("primer3_R:",primer3_R)
        		print(y)
        		print(tm)
        		break
        
	for y in range (0,n0-s):
    		R4 = dna4[-s-y:-s] + dna4_1_overlap
    		seq = R4
    		primer4_R = get_rc(seq)
    		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
   
   	 	y = 0
    		while tm < 60:
        		R4 = dna4[-s-y:-s] + dna4_1_overlap
        		seq = R4
        		primer4_R = get_rc(seq)
        		tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6) 
        		y += 1
    	else:
        		print("primer4_R:",primer4_R)
        		print(y)
        		print(tm)
        		break

## 황종현 

	from Bio.Restriction import *
	from Bio.SeqUtils import MeltingTemp as mt
	from Bio.Seq import Seq
	import sys, numpy as np
	import os
	import pandas as pd
	import re
	import requests
	import json
	
	### Sequence Input
	my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGGTGGCGATCGCCGAAGGAGTCCGCTCGAATCGGGCTCCTAGCTGATATTCGATCGATTGCCCCTAAGCTAGCTATCATCCCTAGCCTTAATATTCTCTCGCGCAGATCGATCGGGCAATATCGATCGGATCCGATCCGAAAGCCTAATCGAATCTCTAGAGCTAGCTAATTCGATCGATCTCCTAGAGCTCTAGCTAGCTTTGGGC")
	print("Sequence length :",len(my_seq))

	### Fragment Number Input
	n = int(input ("fragment 갯수 :"))

	### Overlap Length Input
	s = int(input ("overlap 길이 :"))

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

	print("\n")

	### Overlap + DNA Fragment 서열 생성
	mod = sys.modules[__name__]

	#get_fragment start site
	for i in range(1,n+1):
	    if i < n:
	        a = round(len(my_seq)/n) * i + s
	        globals()['df_{}'.format(i)] = a
	    if i == n:
	        a = len(my_seq)
	        globals()['df_{}'.format(i)] = a
	    print("fragment start site %d:" % i, a)
    
	print("\n")

	###get_overlap + DNA sequence
	for x in range (0,n+1):
 	   y = 0
 	   if x == 0:
	        globals()['dna__overlap_{}'.format(x)] = my_seq[0:y+s]
	    if x == 1:
	        b = my_seq[y:(getattr(mod, 'df_{}'.format(x), x))]
	        globals()['dna__overlap_{}'.format(x)] = b
 	       c = my_seq[(y+((getattr(mod, 'df_{}'.format(x), x))-s)):(y+(getattr(mod, 'df_{}'.format(x), x)))]
 	       globals()['overlap_{}'.format(x)] = c
        
  	      seq = getattr(mod, 'overlap_{}'.format(x))
 	       if gc < 0.4 or gc > 0.6 and Tm > 60:
 	           y += 1
 	       else:
 	           print("DNA %d: " % x, getattr(mod, 'dna__overlap_{}'.format(x)),"\n", "overlap %d & %d :" % (x, x+1), seq,"\n")
            
 	   if 1 < x < n: 
 	       bb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
	        globals()['dna__overlap_{}'.format(x)] = bb
	        cc = my_seq[(y+(getattr(mod, 'df_{}'.format(x), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
	        globals()['overlap_{}'.format(x)] = cc
        
 	       seq = getattr(mod, 'overlap_{}'.format(x))
        
 	       if gc < 0.4 or gc > 0.6 and Tm > 60:
 	           x += 1
 	       else:
 	           print("DNA %d: " % x, getattr(mod, 'dna__overlap_{}'.format(x)),"\n", "overlap %d & %d :" % (x, x+1), seq,"\n")
            
 	   if x == n:
  	      bbb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(len(my_seq))] + (dna__overlap_0)
  	      globals()['dna__overlap_{}'.format(x)] = bbb
  	      ccc = my_seq[y:(y+s)]
  	      globals()['overlap_{}'.format(x)] = ccc 
        
   	     seq = getattr(mod, 'overlap_{}'.format(x))
        
   	     if gc < 0.4 or gc > 0.6 and Tm > 60:
   	         y += 1
   	     else:
   	         print("DNA %d: " % x, getattr(mod, 'dna__overlap_{}'.format(x)),"\n", "overlap %d & %d :" % (x, 1), seq,"\n")
    

## Reference code for testing Assembly Fragments
* https://github.com/BjornFJohansson/pydna/blob/6dd22c4a3708552220c2c52c712a23d951eca743/tests/test_module_design.py
---
## Reference
* [NEB Golden Gate Assembly Tool](https://goldengate.neb.com/)
