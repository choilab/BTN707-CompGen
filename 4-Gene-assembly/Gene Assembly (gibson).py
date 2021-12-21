#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
xyz = input("Sequence 입력 :") 
my_seq = Seq(xyz)
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

dna_overlap_list = []
overlap_list = []

x = 0
y = 0
while x < (n+1) and y < (n+1):
    if x == 0:
        dna__overlap = my_seq[0:y+s]
        overlap = my_seq[0:y+s]
        
    if x == 1:
        b = my_seq[y:(getattr(mod, 'df_{}'.format(x), x))]
        dna__overlap = b
        c = my_seq[(y+((getattr(mod, 'df_{}'.format(x), x))-s)):(y+(getattr(mod, 'df_{}'.format(x), x)))]
        overlap = c
                
    if 1 < x < n: 
        bb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
        dna__overlap = bb
        cc = my_seq[(y+(getattr(mod, 'df_{}'.format(x), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
        overlap = cc
            
    if x == n:
        bbb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(len(my_seq))] + dna_overlap_list[0]
        dna__overlap = bbb
        ccc = my_seq[y:(y+s)]
        overlap = ccc 
        
        #seq = getattr(mod, 'overlap_{}'.format(x))
        
    overlap_tm = mt.Tm_NN(overlap, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
    overlap_gc = check_GC(overlap)
    
    print(overlap, overlap_tm)

    if overlap_tm < 60 and overlap_gc > 0.4 and overlap_gc < 0.6:
        dna_overlap_list.append(dna__overlap)
        overlap_list.append(overlap)
        x += 1
        y = 0
    else:
        y += 1
        
print("overlap + dna fragment :", dna_overlap_list[1:], "\n","overlap:", overlap_list)
exit()


# In[ ]:


GATCGATGGGCCTATATAGGATCGAAAATCGGTGGCGATCGCCGACTAGGGCTTCGATGCGATGCATATCGCGCGATCGATCGATCGATTTACGTAGCGTAGCTGATGCTTAAGGAGTCCGCTCGAATCGGGCTCCTAGCTGATATTCGATCGATTGCCCCTAAGCTAGCTATCATCCCTAGCCTTAATATTCTCTCGCGCAGATCGATCGGGCAATATCGATCGGATCCGATCCGAAAGCCTAATCGAATCTCTAGAGCTAGCTAATTCGATCGATCTCCTAGAGCTCTAGCTAGCTTTGGGC
        
            
      while x < (n+1):
    if x == 0:
        globals()['dna__overlap_{}'.format(x)] = my_seq[0:y+s]
        globals()['overlap_{}'.format(x)] = my_seq[0:y+s]
        
        d = mt.Tm_NN(getattr(mod, 'overlap_{}'.format(x)), dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        globals()['overlap_tm_{}'.format(x)] = d
        
        e = check_GC(getattr(mod, 'overlap_{}'.format(x)))
        globals()['overlap_gc_{}'.format(x)] = e
        
    if x == 1:
        b = my_seq[y:(getattr(mod, 'df_{}'.format(x), x))]
        globals()['dna__overlap_{}'.format(x)] = b
        c = my_seq[(y+((getattr(mod, 'df_{}'.format(x), x))-s)):(y+(getattr(mod, 'df_{}'.format(x), x)))]
        globals()['overlap_{}'.format(x)] = c
        
        d = mt.Tm_NN(getattr(mod, 'overlap_{}'.format(x)), dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        globals()['overlap_tm_{}'.format(x)] = d
        
        e = check_GC(getattr(mod, 'overlap_{}'.format(x)))
        globals()['overlap_gc_{}'.format(x)] = e
                
    if 1 < x < n: 
        bb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
        globals()['dna__overlap_{}'.format(x)] = bb
        cc = my_seq[(y+(getattr(mod, 'df_{}'.format(x), x)-s)):(y-1+(getattr(mod, 'df_{}'.format(x), x)))]
        globals()['overlap_{}'.format(x)] = cc
        
        d = mt.Tm_NN(getattr(mod, 'overlap_{}'.format(x)), dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        globals()['overlap_tm_{}'.format(x)] = d
        
        e = check_GC(getattr(mod, 'overlap_{}'.format(x)))
        globals()['overlap_gc_{}'.format(x)] = e
            
    if x == n:
        bbb = my_seq[(y+(getattr(mod, 'df_{}'.format(x-1), x)-s)):(len(my_seq))] + (dna__overlap_0)
        globals()['dna__overlap_{}'.format(x)] = bbb
        ccc = my_seq[y:(y+s)]
        globals()['overlap_{}'.format(x)] = ccc 
        
        seq = getattr(mod, 'overlap_{}'.format(x))
        
        d = mt.Tm_NN(getattr(mod, 'overlap_{}'.format(x)), dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        globals()['overlap_tm_{}'.format(x)] = d
        
        e = check_GC(getattr(mod, 'overlap_{}'.format(x)))
        globals()['overlap_gc_{}'.format(x)] = e

    if getattr(mod, 'overlap_tm_{}'.format(u)) < 60 and 0.4 < getattr(mod, 'overlap_gc_{}'.format(u)) < 0.6:
        x += 1
        y = 0
        continue
    else:
        y += 1
        continue


# In[ ]:


# get primer sequence
def primer_sequence(seq):
    """ primer sequence for each fragment """
     
for x in range(1,n0-s):
     if tm < 60:
        primer1_F = dna4_1_overlap + dna1[s:s+x]
        seq = primer1_F
        tm = mt.Tm_NN(seq, dnac1 = 50, Na = 10, K = 10, Mg = 2, dNTPs = 0.6)
        x += 1
    else:
        print(seq)
        print(tm)
        print(x)
        break    


# In[2]:


len('GATTGCCCCTAAGCTAGCTAT')


# In[ ]:




