#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Restriction import *
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import numpy as np
import os
import pandas as pd
import re
import requests
import json


# In[2]:


#overhang

def get_Gibson_overlap(dnaseq, enzyme_list, direction, preserve_cut=True):
    seq = Seq(dnaseq['bases'])
    Ana = Analysis(CommOnly, seq, linear=False)
    
    """ Returns the overlapping dna sequence for Gibson assembly
    From the enzyme list it will grab 60 nts from the start and end for the 
    Gibson overlap
    Args:
        dnaseq: dna sequence to check
        enzyme_list: restriction enzymes to cut [start, end] (order matters)
        direction: direction of the inserted region
        preserve_cut: whether or not to preserve the restriction enzyme site
    Returns:
        overhang_list: list of the left and right gibson overhang
        linker_list: extra bases to preserve the restriction site
    """
    
    overhang_list = []
    linker_list = []
    for enzyme, d in zip(enzyme_list, [1,0]):
        exec('cut_template = {}.elucidate()'.format(enzyme))
        # Location of cut
        value = Ana.with_name([enzyme]).values()[0]
        
        # Length of cut to preserve cut_site
        cut_site = cut_template.replace('_', '').find('^')
        cut_site = len(clean_seq(cut_template)) - cut_site
        
        # Correct which side to cut
        assert(len(value)==1), 'Enzyme is not a single cutter'
        if d==0:
            value[0] += cut_template.find('_') - cut_template.find('^') - 1
        overhang = seq[value[0]-1-60*d:value[0]-1+60*(not d)] # -1 due to offset index
        linker = seq[value[0]-1-60*(not d):value[0]-1+60*d] # -1 due to offset index
        linker = str(linker)
        linker = [linker[:cut_site*(2*d-1)],linker[cut_site*(2*d-1):]][::-direction]
        if d == 0:
            overhang = overhang.reverse_complement()
            linker = [get_rc(x) for x in linker]
        overhang_list.append(str(overhang))
        linker_list.append(linker)
    return overhang_list, linker_list


# In[3]:


def get_anneal_insert(dna_insert, label_insert, direction,
                      insert5p='', insert3p='', target_Tm=60, delta_Tm=1.5, 
                      GC_bound=[0.4, 0.6], GC_3prime=True, linker_protein=True, 
                      verbose=False):
    """ Returns the annealing sequence (PCR region)
    
    Args:
        dnaseq: dna sequence to check
        label_insert: region to anneal (to PCR)
        direction: direction of label_insert
        insert5p: bases or amino acids to add to the 5' end
        insert3p: bases or amino acids to add to the 3' end
        target_Tm: target melting tempearture for PCR in Celcius
        delta_Tm: margin of error from the target melting temperature
        GC_bound: boundary for acceptable GC content [low, high]
        GC_3prime: boolean indicating 3 prime end contains a G or C
        linker_protein: boolean on whether the insert5p and 3p are amino acids or bases
        verbose: boolean
        
    Returns:
        anneal_list: sequence for the PCR annealing
        insert_list: sequence for for the 5' and 3' insert
        boolean on whether or not it worked
    """

    aa2codon, codon2aa = load_m_codon()
    region = [x for x in dna_insert['annotations'] if x['name'] == label_insert][0]
    idx_list = [region['start'], region['end']]
    gene_seq = dna_insert['bases'][idx_list[0]:idx_list[1]].upper()
    insert_list = ['', ''] # 5' insert, 3' insert (both are written 5' -> 3')
    anneal_list = ['', ''] # annealing region for 5' end and 3' end (both are written 5' -> 3')

    # Generate linker region
    if linker_protein:
        if insert5p:
            insert_list[0] += generate_aa_codon(insert5p)
        if insert3p:
            insert_list[1] += get_rc(generate_aa_codon(insert3p))
    else:
        insert_list[0] += insert5p
        insert_list[1] += insert3p # Make sure it's reverse complement of what you want


    # Generate annealing region
    if target_Tm < 58:
        print ('Warning: Target melting tempearture is low. Ideally 60-80 °C')
    elif target_Tm > 82:
        print ('Warning: Target melting temperature is high. Ideally 60-80 °C')

    for pos in range(2):
            temp_seq = ''
            for i in range(1,61):
                if pos:
                    temp_seq = get_rc(gene_seq[-i:])
                else:
                    temp_seq = gene_seq[:i]
                if check_anneal(temp_seq, target_Tm=target_Tm, delta_Tm=delta_Tm, GC_bound=GC_bound, GC_3prime=GC_3prime, verbose=verbose):
                    if verbose:
                        print ('Annealing GC Content: ', check_GC(temp_seq))
                        print ('Annealing Tm: ', get_Tm(temp_seq))
                        print ('Length: ', len(''.join(temp_seq)))
                        print (''.join(temp_seq) + '\n')
                    break
                if i == 60:
                    print ('Manual design of annealing region is required')
                    return anneal_list, insert_list, False
            anneal_list[pos] += temp_seq
    return anneal_list, insert_list, True


# In[4]:


def get_primer(overhang_list, linker_list, insert_list, anneal_list, direction, gibson_overhang=20):
    """ Combines all the lists to construct the full primer
    Args:
        overhang_list: list of the left and right gibson overhang
        linker_list: extra bases to preserve the restriction site
        insert_list: sequence for for the 5' and 3' insert (for adding more amino acids, etc)
        anneal_list: sequence for the PCR annealing
        direction: direction to insert
        gibson_overhang: length of desired Gibson overhang (20 is ideal)
            if the primer is too long it will shorten it but it will notify you if < 15 nts	Returns
        primer_list containing the forward and reverse primer both written as 5' to 3'
    """
    
    primer_list = []
    for i in range(2):
        primer = [overhang_list[::direction][i], linker_list[::direction][i][(i+1)%2], insert_list[i], anneal_list[i]]
        primer = [primer[0].upper(), primer[1].lower(), primer[2].lower(), primer[3].upper()]# insert and linker is lowercase
        temp_primer = ''.join(primer[1:])
        temp_length = len(temp_primer)

        # Correct for gibson overhang
        if (temp_length + gibson_overhang) > 60:
            gibson_overhang = 60 - temp_length
            if gibson_overhang < 15:
                print ('Warning. Since primer is too long Gibson overlap is now {}.'.format(gibson_overhang))
        
        overlap = primer[0][-gibson_overhang:]
        temp_primer = ''.join([overlap, temp_primer])
        primer_list.append(temp_primer)
    return primer_list


# In[5]:


def primer_design(plasmid_base, label_remove, insert, label_insert, delta=3,
                insert5p='', insert3p='', target_Tm=60, delta_Tm=0.75, 
                GC_bound=[0.4,0.6], GC_3prime=True,linker_protein=True, 
                verbose=False, new_plasmid_name='New', create_plasmid=False):

    # Step 0. Load the dna files and their id
    folder2dna, dna2id = get_folder2dna2id(projectId=None)

    # Step 1. Find restriction enzymes

    # Remove DNA for insert
    dnaseq = get_sequence(dna2id[plasmid_base])
    start_cut, end_cut, direction = get_cutsite(dnaseq, label_remove, delta=delta, verbose=verbose)

    # Step 2. Pick out 2 enzymes for cutting the 5' and 3' end
    final_enzyme = [start_cut[0], end_cut[0]]
    for enzyme in final_enzyme:
        print ('Cut: {}'.format(enzyme))

    # Double check restriction site does not exist in the DNA to be inserted
    # dna_insert = get_sequence(dna2id[insert])
    # if check_cutsite(dna_insert, enzyme_list):
    # print 'Pick different enzymes'

    # Step 3. Get overlap sequence for Gibson
    overhang_list, linker_list = get_Gibson_overlap(dnaseq, final_enzyme, direction)

    
    # Step 4. Design annealing region for primer on the insert
    dna_insert = get_sequence(dna2id[insert])
    status = False # Try to search more Tms to find anneal
    anneal_list, insert_list, status = get_anneal_insert(dna_insert, label_insert, direction, 
                        insert5p=insert5p, insert3p=insert3p, target_Tm=target_Tm, 
                        delta_Tm=delta_Tm, GC_bound=GC_bound, GC_3prime=True, 
                        linker_protein=linker_protein, verbose=verbose)

    # Step 5. Put together the primer
    primer_list = get_primer(overhang_list, linker_list, insert_list, anneal_list, direction)
    print ('Forward primer: {} ({} nts)'.format(primer_list[0], len(primer_list[0])))
    print ('Reverse primer: {} ({} nts)'.format(primer_list[1], len(primer_list[1])))

    if create_plasmid:
        return create_plasmid_file(primer_list, direction, plasmid_base, label_remove, insert, label_insert, final_enzyme, new_plasmid_name)
    return primer_list


# In[ ]:




