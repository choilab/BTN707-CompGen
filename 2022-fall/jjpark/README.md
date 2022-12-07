# Web Application for one-touch RNA-seq analysis 
## Purpose 
+ RNA-seq data analysis workflow는 아래와 같음.
 1. Sequencing reads
 2. Trimming & Quality Control (TrimGalore)
 3. Alignment to reference genome (HISAT2,STAR,Bowtie2)
 4. Count gene features (gene level analysis) (Feature Count, edgeR)
 5. Differential gene expression 
 6. Stastical analysis 
 7. Enrichment analysis (Enrichr, GSEA)

+ 위의 과정을 통합하여, 한번의 클릭을 통해 1~6의 과정을 진행하는 웹 애플리케이션의 개발을 목적으로 한다. 

## Tools 
+ 본 연구에서 사용되는 Tools는 아래와 같다.
  + 웹 어플리케이션 제작을 위한 Tool로서 Python Django를 사용함.
  + Trimming & Quality Control을 위한 Tool로서 TrimGalore를 사용함.
  + Alignment를 위한 Tool로서 HISAT2를 사용함.
  + Count gene features 제작을 위한 Tool로서 (Feature Count/edgeR)를 사용함.
  + Stastical analysis를 위한 Tool로서 GEO2R을 사용함.
 
## Additional Functions
+ Paired read와, one-way read의 Input 모두 handling 해야함.
+ Model animal(Human, Zebra fish, Mouse 등..)의 경우 input으로 reference genome의 gff,fa 파일을 넣어주지 않고, running할 수 있는 환경을 만들어야함.
+ SRA serial number을 넣어줄 때, SRA 데이터를 다운로드해 running하게 해야함.
+ GEO2R의 소스코드를 사용해 gene count table을 input으로 간단한 통계를 제공해야함.

## RNA-seq 
RNA-seq is a technique for analysis transcriptome and difference in expression. According to central dogma(1958, Francis Harry Compton Crick), transcript(mRNA) transfer to protein. RNA-seq is a method judging that the higher the number of transcripts, the more expression.
The RNA-seq workflow is shown in the figure below.  

![image](https://user-images.githubusercontent.com/97942772/206076146-42bd9580-c9e9-4512-ba3e-a34089f32777.png)

(Wang et. al, RNA-Seq: a revolutionary tool for transcriptomics, Nat. Rev. Genetics 10, 57-63, 2009))
 
 Extract mRNA from query sample. After fragmenting mRNA or synthesizing cDNA with mRNA, create a library by attaching necessary sequences for sequencing such as adapters. Perform a NGS(Next generation sequencing), generate short sequencing data, called read.
 Next stage for RNA-seq is a mapping, attach read to the reference sequence (species from this sample originated). (Wang et al,.(2019)) 
