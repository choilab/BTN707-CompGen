# 2021 Fall BTN707 Computational Genomics

## Term projects

* Windows10 users - if you like to use `linux` (unix) environment, install [WSL Windows Subsystem for Linux](https://docs.microsoft.com/ko-kr/windows/wsl/install)
* for python coding: use [`conda`](https://www.anaconda.com/products/individual) - virtual environment control - and [`Pycharm`](https://www.jetbrains.com/ko-kr/pycharm/download/) - Integrated Development Environment (IDE), 통합개발환경
* All individual projects will be maintained in the [Github `BTN707` repository](https://github.com/choilab/2021-compgen-class/)
---
1. CRISPR Genome Editing - Prediction of On/Off Target & gRNA designer
- Input: microbial genome sequence (.fna/.fasta nucleotide)
- Output: target/off-target site (.coordinate)
- Options: # of mismatches/positional mismatches/insertion/deletion/base ambiguity
- What/Why is it important? How can it be designed/built/tested? 
- Reference program - [CAS-off-finder http://www.rgenome.net/cas-offinder/](http://www.rgenome.net/cas-offinder/)

---
2. Anti-sense oligonucleotide (ASO) off-target finder - Almost similar to CAS9-off-finder
- Input: microbial genome sequence (.fna/.fasta nucleotide)
- Output: target/off-target site (.coordinate)
- Options: # of mismatches/positional mismatches/insertion/deletion/base ambiguity
- What/Why is it important? How can it be designed/built/tested? 
- Reference program - [GGGenome https://gggenome.dbcls.jp/](https://gggenome.dbcls.jp/)

---
3. Open Reading Frame (ORF) finder
- Input: microbial genome sequence (.fna/.fasta nucleotide)
- Output: All possible open reading frames (.faa amino acids/.coordinate)
- Options: strandedness/ATG/no-ATG
- What/Why is it important? How can it be designed/built/tested?
- Reference program - [ORFfinder https://www.ncbi.nlm.nih.gov/orffinder/](https://www.ncbi.nlm.nih.gov/orffinder/)

---
4. Gene Assembly Designer
- Input: gene
- Output: a pool of variable lengths of oligos (overlapped) for synthetic full gene
- Options: overlap length/# of fragments/restriction site removal
- What/Why is it important? How can it be designed/built/tested?
- Reference program - [Assmebly PCR oligo Maker](https://academic.oup.com/nar/article/33/suppl_2/W521/2505480)

