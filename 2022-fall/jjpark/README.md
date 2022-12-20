# OCRWA (One - Click RNA-seq pipeline Web APP)
## Purpose of WebApp
Computational processes (adapter trimming, aligning, counting) may not be easy for wet lab scientist. So that we service Wep App which can process all computational processes. As a result of this web application, User can get gene count table with one-click.

<img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/208585551-f58d4257-5af4-44bd-93fd-e07d6294022c.png">

## Usage
+ We service on [leafeon.korea.ac.kr:8001](http://leafeon.korea.ac.kr:8001/). 

## Programs used for WebApp
 + Trimming & Quality Control : [TrimGalore (v0.6.6)](https://github.com/FelixKrueger/TrimGalore)
 + Alignment to reference genome : [HISAT2 (v2.2.1)](http://daehwankimlab.github.io/hisat2/)
 + Count gene fetures : [FeatureCount (v2.0.0)](https://rnnh.github.io/bioinfo-notebook/docs/featureCounts.html)
 + WebApplication : [Shiny for python (v alpha)](https://shiny.rstudio.com/py/)

## Requirement for launching.
 + [TrimGalore (v0.6.6)](https://github.com/FelixKrueger/TrimGalore)
 + [HISAT2 (v2.2.1)](http://daehwankimlab.github.io/hisat2/)
 + [FeatureCount (v2.0.0)](https://rnnh.github.io/bioinfo-notebook/docs/featureCounts.html)
 + [Shiny for python (v alpha)](https://shiny.rstudio.com/py/)
 + We made index for alignment in some model animals, Homo sapiens, Mus musculus, Danio rerio. Please download FNA file of these animals in [NCBI refseq](https://www.ncbi.nlm.nih.gov/refseq/), and use command "hisat2-build" to make index of them before launching.

<br>
</br>

------------------------------------------------
------------------------------------------------
# ABOUT RNA-seq
## RNA-seq 
RNA-seq is a technique for analysis transcriptome and difference in expression. According to central dogma(1958, Francis Harry Compton Crick), transcript(mRNA) transfer to protein. RNA-seq is a method judging that the higher the number of transcripts, the more expression.
The RNA-seq workflow is shown in the figure below.  

![image](https://user-images.githubusercontent.com/97942772/206076146-42bd9580-c9e9-4512-ba3e-a34089f32777.png)

[Reference : Wang et. al, RNA-Seq: a revolutionary tool for transcriptomics, Nat. Rev. Genetics 10, 57-63, 2009)](https://www.nature.com/articles/nrg2484)
 
 Extract mRNA from query sample. After fragmenting mRNA or synthesizing cDNA with mRNA, create a library by attaching necessary sequences for sequencing such as adapters. Perform a NGS(Next generation sequencing), generate short sequencing data, called read.
 Next stage for RNA-seq is a mapping, attach read to the reference sequence (species from this sample originated). Wang et al,.(2019)) It suggests that the more read attached to a specific gene, the more expression in that gene. 
 
## RNA-seq roadmap
The figure below explains comprehensive roadmap for experimental design and analysis using Illumina sequencing.

<br/>

![image](https://user-images.githubusercontent.com/97942772/206102252-0cc8748a-8050-4d07-ae91-a6a5724faeda.png)  


[Reference : Conesa, A., Madrigal, P., Tarazona, S. et al. A survey of best practices for RNA-seq data analysis. Genome Biol 17, 13 (2016).](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8)]

After sequencing, for differentially expressed genes(DEGs) analysis, several computational processes are required. 
Computational processes are divided into Quality control, Read alignment, Quantification.
### Quality Control
Raw read quality control(QC) is a process that checks sequence quality, GC content, adaptor presence, excessive k-mer presence, duplicated read, etc. for sequencing error, PCR artifact, contamination. (Conesa, A. et al.(2016))
Low quality bases/reads are get rid off during quality control. The representative software is FASTQC.
### Read Alignment 
In this step, filtered reads are aligned to reference genome. One of the most important parameter is overall alignment rate. If few reads are contaminated, so that read sequence contain sequences which is derived from other species, the rate of alignment of the reference genome is low. Additionally, alternative splicing should be considered.
The FASTQ file format, the format for raw reads with containing quality score and sequence information, used as input. Additionally reference genome's FASTA format file is required also. After read alignment, user get BAM format file as a output. Which containing location of reference genome, sequence of query read, mapping quality. The representative softwares are STAR, HISAT2.
### Quantification
Reading BAM file let us obtain expression for each gene. BUt we can't use this raw count table, because raw count doesn't consider transcript's length, total read's count, sequencing bias. For example, if the gene length of the reference genome is long, a lot of reads will be bound probably. So normalization step is necessary. Below table is showing few normalize value for quantification. After quantification, 

|Normalized value|description|Equation|
|-|-|-|
|RPKM|reads per kilobase of exon model per million reads|numReads / ( geneLength/1000 * totalNumReads/1,000,000 )|
|FPKM|fragment per kilobase of exon model per million mapped reads|numFragment / ( geneLength/1000 * totalNumFragments/1,000,000 )|
|TPM|transcript per million|10^6 * RPKM/Sum(RPKM)|

[ZZhao S, Ye Z, Stanton R. Misuse of RPKM or TPM normalization when comparing across samples and sequencing protocols. RNA. 2020 Aug;26(8):903-909.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7373998/)

Few softwares stands for quantification, Featurecounts, edgeR.

<br/>

After all these processes, User can get normalized expresseion dataset, which is available for analysis and visualizaiton.

<br/>

