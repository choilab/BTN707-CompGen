# Lactobacillus Genome Statistics (NCBI, October 16, 2025)

An updated summary of Lactobacillus genomes available on the NCBI Assembly Genome Browser, including registration, availability for download, and annotation status. This table also includes the official reference genome count.

| Category                                   | Count  | Description                                                                |
| ------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| Total genome assemblies                     | 5,427  | All registered Lactobacillus genomes (includes drafts and complete)        |
| Downloadable genome assemblies              | 5,427  | All assemblies can be downloaded directly via NCBI datasets portal         |
| Annotated genomes (GenBank/RefSeq)          | 3,329  | Assemblies with annotation either from GenBank submitters or NCBI RefSeq   |
| NCBI RefSeq-annotated genomes               | 2,326  | Assemblies specifically annotated by NCBI RefSeq, usually via PGAP         |
| Official reference genomes                  | 49     | Genomes officially designated as NCBI Reference Genomes                    |

- Most annotated genomes have both GenBank submitter and NCBI RefSeq annotation
- “NCBI RefSeq-annotated” means annotation by NCBI using their Prokaryotic Genome Annotation Pipeline (PGAP)
- “Reference genomes” are curated, high-quality representatives for each species

> Data source:  
> [NCBI Lactobacillus Assembly Genome Browser (taxon 1578)](https://www.ncbi.nlm.nih.gov/datasets/genome/?taxon=1578) (Accessed: 2025-10-16)[118][119][120]

- Use the web UI and select:
    - **Source:** "All" 
    - **Assembly level:** Chromosome and Complete
    - **File types:** FASTA, GTF, GFF, GBFF, CDS FASTA, Protein FASTA, Assembly report

> The downloadable file will be named `ncbi_dataset.zip`.

>주요 결과 요약
항목	개수	설명
초기 다운로드 유전체	2,976개	Lactiplantibacillus plantarum 종 전체
최종 대표 균주	195개	SKANI 100% ANI 기준으로 중복 제거 완료
