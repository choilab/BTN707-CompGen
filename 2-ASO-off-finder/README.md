# Antisense oligonucleotide (ASO) off-target finder

ASO-off-finder is a program that finds target and potential off-target sites in the FASTA sequence for input antisense oligonucleotide (ASO) sequences.

# Table of Content

* [Students](#student)
* [Program overview](#overview)
* [Thinkabouts](#intro)
  * [What is the problem to solve?](#intro2)
  * [Why is the problem biologically important?](#intro3)
* [Update history](#history)
* [Algorithm outline](#outline)
* [Benchmark test](#benchmark)

<a name="student"></a>
# Students

* 김보근
* 박연수

<a name="overview"></a>
# Program overview

* Input: target RNA sequence and oligonucleotide sequence (FASTA format)
* Output: target and off-target site coordinate, the number of mismatches in the alignment
* Options: # of allowed mismatches/indels

<a name="intro"></a>
# Thinkabouts
<a name="intro2"></a>
## What is the problem to solve?

Finding target and off-target site of antisense oligonucleotides.

### What is Antisense oligonucleotide (ASO)?

Antisense oligonucleotide (ASO) is a short, synthetic, single-stranded oligonucleotide. ASOs are intended to bind to RNA (coding or non-coding) molecules with complementary sequences.[^1]
[^1]: [Rinaldi, C., & Wood, M. J. (2018). Antisense oligonucleotides: the next frontier for treatment of neurological disorders. Nature Reviews Neurology, 14(1), 9-21.](https://doi.org/10.1038/nrneurol.2017.148)

![](./supplement/ASO_mechanism.png)

By this method, ASOs can modify protein expression or activity of RNAs through several different methods[^1]:
* Target RNA degradation by RNAse H
* Translational arrest
* Inhibit RNA-binding proteins
* RNA splicing modulation
* Increased translational activity

### Different types of standard ASOs

**1\. Gapmer ASO**

![](./supplement/Gapmer_ASO.png)

Gapmer ASOs have modifications in the phosphate backbone to support RNAse H activity and in the sugar (ribose) ring for higher affinity (e.g. LNA).

Modified nucleotides are only present in the wing of ASOs. Normal nucleotides are present about 10 bases in the central region. Target RNA sequence is cleaved by RNAse H.[^2]

[^2]: [DeVos, S. L., & Miller, T. M. (2013). Antisense oligonucleotides: treating neurodegeneration at the level of RNA. Neurotherapeutics, 10(3), 486-497.](https://doi.org/10.1007/s13311-013-0194-5)

**2\. Splice-switching ASO**

![](./supplement/Splice_ASO.jpeg)

Splice-switching ASOs does not use RNAse H-mediated cleavage of target RNAs. Instead, it sterically blocks the target RNA and regulate pre-mRNA splicing and repairing of defective RNA.[^3]

[^3]: [Havens, M. A., & Hastings, M. L. (2016). Splice-switching antisense oligonucleotides as therapeutic drugs. Nucleic acids research, 44(14), 6549-6563.](https://doi.org/10.1093/nar/gkw533)

<a name="intro3"></a>
## Why is the problem biologically important?
### ASO therapy

ASO can be used to inhibit RNA with specific sequences, which leads to the fact that ASOs could be helpful to treat diseases resulting from single mutant proteins. Several ASO therapies are already approved by FDA for rare genetic diseases:
* Kynamro - Familial hypercholesterolemia
* Tegsedi - Hereditary ATTR amyloidosis
* Exondys 51 - Duchenne muscular dystrophy
* Spinraza - Spinal muscular atrophy

### Why find ASO off-target sites?

Specific ASO binding to the target RNA sequence is needed for high selectivity. However, there is a chance that ASO might bind to off-target RNA molecules that have similar sequences to the original target RNA. This off-target binding of ASOs might cause unintended toxicity.

Also, animal studies cannot be used for off-target finding of ASO applied to humans because of diiference in the genome sequence between.

Thus, in silico analysis using the human RNA database followed by in vitro expression analysis using human cells are essential.

<a name="history"></a>
# Update history
## ASO-off-finder v1.0 (2021/11/17)
* First version of ASO-off-finder
* Uses dynamic programming for approximate sequence alignment. [Description slides from Cousera lecture](./supplement/Dynamic_programming.pdf)
* Jupyter notebook file of ASO-off-finder could be found in [v1.0 folder](./v1.0/aso_off_target.ipynb).

## ASO-off-finder v1.1 (2021/12/01)
* Shorter run time using CPU multiprocessing by implementing `concurrent.futures` module
* Input multiple RNA/ASO sequences by FASTA format files
* Human spliced/pre-spliced mRNA sequences can be downloaded from [D3G database](https://d3g.riken.jp/release/18.04/)

## ASO-off-finder v2.0 (2021/12/08)
* Index RNA sequences and skip sequences with any available index matches
* Aligned sequences are shown in output file

<a name="outline"></a>
# Algorithm outline

![image](https://user-images.githubusercontent.com/69707020/145952837-ab7720ff-69f8-452b-97dc-b3e0a8fd890d.png)

Problem | Query | Reference
---- | ---- | ----
Read alignment problem | Sequenced reads | Reference genome
ASO off-target finder | ASO sequence | Target RNA sequence database

* Finding ASO off-target sites is similar to the read alignment problem
* Apply dynamic programming for approxiamte alignment for matching ASO sequence to target RNA sequences

# Benchmark test
## ASO-off-finder v1.1
* Used dataset: RefSeq Human aggregated spliced mRNA sequence, release 18.04 [D3G database](https://d3g.riken.jp/release/18.04/)
* Compare result from reference tool, [gggenome](https://gggenome.dbcls.jp/), and ASO-off-finder's output
* Use first 20~21 nucleotide sequence from human mRNA sequence as artificial ASO sequences for benchmark test

Original gene | Sequence | Length
---- | ---- | ----
CD4 | GTTTGGGGCCGGCCCAGGCCT | 20 nt
CXCL1 | CACCCCAGCCCTATCCCTTT | 21 nt

![](./v1.1/gggenome_result_CD4.png)

    match_site	mismatch_number	alignment_number
    NM_000616.4,NM_001195014.2,NM_001195015.2,NM_001195016.2,NM_001195017.2	2	2
    NM_000616.4,NM_001195014.2,NM_001195015.2,NM_001195016.2,NM_001195017.2	1	2
    NM_000616.4,NM_001195014.2,NM_001195015.2,NM_001195016.2,NM_001195017.2	0	1
    NM_014240.2	2	1

* ASO-off-finder successfully found the same perfect match from CD4 mRNAs and match from LIMD1 (NM_014240.2) mRNA with 1 mismatch and 1 indel

![](./v1.1/gggenome_result_CXCL1.png)

    match_site	mismatch_number	alignment_number
    NM_001511.3,NR_046035.1	2	2
    NM_001511.3,NR_046035.1	1	2
    NM_001511.3,NR_046035.1	0	1
    NM_002090.2	2	1
    NM_002089.3	2	3

* Same result from perfect match from CXCL1 mRNAs and match from CXCL2/3 mRNAs with 2 mismatches

## ASO-off-finder v2.0
* Same dataset (RefSeq Human spliced mRNA aggregated, release 18.04) was used for benchmark test
* Used sequence from CD4 gene from the ASO-off-finder v1.1 benchmark test

Original gene | Sequence | Length
---- | ---- | ----
CD4 | GTTTGGGGCCGGCCCAGGCCT | 20 nt

![](./v1.1/gggenome_result_CD4.png)

    NM_000616.4,NM_001195014.2,NM_001195015.2,NM_001195016.2,NM_001195017.2
    GTTTGGGGCCGGCCCAGGCCT
    GTTTGGGGCCGGCCCAGGCCT
    NM_014240.2
    GTTTGGGGCCGGCCCAGGCCT
    GTTTGGGGCTGGCC-AGGCCT
    
* ASO-off-finder v2.0 shows the same alignment for LIMD1 (NM_014240.2) mRNA with 1 mismatch ('C' > 'T') and 1 indel ('C' > '-')

Program version | Running time
---- | ----
ASO-off-finder v1.1 | > 3 min
ASO-off-finder v2.0 | 1 min 36 seq
gggenome website | < 10 seq

* Also, ASO-off-finder v2.0 is more than two times faster than version 1.1
