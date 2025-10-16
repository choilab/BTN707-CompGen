# _Staphylococcus epidermidis_ pan-genome
## Using ChatGPT
## 1. how many Staphylococcus epidermidis genomes are publicly available for pan-genome analysis?
There isn't a single fixed number, because it depends on what one counts (complete genomes vs. draft assemblies, with metadata, etc.), and the number keeps increasing. Here’s a summary of what I found, plus an estimate of recent numbers:

---
## What’s known

* The *PubMLST* database for *Staphylococcus epidermidis* lists **~1,189 genome assemblies** as of Sept 2025. ([PubMLST][1])
* A 2020 paper (“Comparative Genome Analysis Reveals the Molecular Basis of Niche Adaptation …”) used **198** publicly available *S. epidermidis* genomes from GenBank. ([Frontiers][2])
* Another study integrating ocular, skin, blood, etc. isolates reported **187** genomes (public + newly sequenced) in that comparative + pan-genome study. ([Frontiers][3])

---

## My estimate as of now

Given that PubMLST reports ~1,189 genome assemblies, that is likely a good current count of publicly available genomes for *S. epidermidis* that are in assembly form. If you limit to only *high-quality complete* genomes (closed chromosomes + associated plasmids, minimal gaps), the number is much smaller (tens to low hundreds).

---

If you tell me your criteria (e.g. complete genomes only, minimum N50, with metadata, or only clinical isolates, etc.), I can give you the number more precisely. Do you want that?

[1]: https://pubmlst.org/organisms/staphylococcus-epidermidis?utm_source=chatgpt.com "Staphylococcus epidermidis | PubMLST"
[2]: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2020.566080/full?utm_source=chatgpt.com "Frontiers | Comparative Genome Analysis Reveals the Molecular Basis of Niche Adaptation of Staphylococcus epidermidis Strains"
[3]: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.770191/pdf?utm_source=chatgpt.com "ORIGINAL RESEARCH"

## how many complete genomes and how can we download them?
I did a survey of public databases — the number of *completely closed* (finished) *Staphylococcus epidermidis* genomes is modest (dozens), rather than in the hundreds. Below is what I found, caveats, and how you can download them.

---

## How many complete genomes are available (estimate + examples)

* The **StaphyloBase** resource reports ~ 42 complete genomes across *Staphylococcus* species (across many species) (while many more draft genomes) ([OUP Academic][1])
* In the *S. epidermidis*–specific literature, some works say “389 reported in GenBank, of which 11 were complete genome sequences (as of that date)” ([PMC][2])
* More recent individual completions include, for example, *S. epidermidis* **CSF41498** (complete with plasmids) ([PMC][3]), *S. epidermidis* **1457** (complete) ([PubMed][4]), *S. epidermidis* **ATCC 12228** (closed) ([PMC][2]), *S. epidermidis* **CCSM0287** (complete) ([PubMed][5]), *S. epidermidis* **B273** (complete) ([PubMed][6]), etc.

Given these, a rough guess is that there are on the order of **a few dozen** high‑quality *complete* *S. epidermidis* genomes publicly available as of now (2025).

If you require a precise up‑to‑date count, one approach is to query NCBI’s Assembly database (filtering for "Complete Genome" status) for *S. epidermidis*.

---

## 2. How to find and download complete genomes

Here’s a step‑by‑step guide you can follow to fetch complete genomes from NCBI (or related public resources):

1. **Query the NCBI Assembly database (or Genome)**

   * Use NCBI Assembly Browser: go to [NCBI Assembly](https://www.ncbi.nlm.nih.gov/assembly) and search for *“Staphylococcus epidermidis”*.
   * Use filters to select *Assembly Level = “Complete Genome”* or *“Chromosome”* (rather than “Scaffold” or “Contig”).
   * You can also use the `esearch` + `esummary` + `efetch` or `datasets` command‑line tools (NCBI Datasets) to retrieve metadata and download links.

2. **Check the assembly status / metadata**

   * Each assembly record will indicate its *Assembly Level* (Complete, Chromosome, Scaffold, Contig), *RefSeq/GenBank status*, *number of contigs*, etc.
   * Only pick those with *Complete Genome* or *“Chromosome + plasmids, fully closed”* status.

3. **Download the genome sequences and annotations**

   * Once you have the assembly IDs (e.g. GCA_ or GCF_ accession), you can download `.fna` (fasta), `.gbff` (GenBank annotation), `.gff` (annotation), etc.
   * Use FTP or HTTPS from NCBI, e.g. from the `ftp.ncbi.nlm.nih.gov/genomes/all/...` path.
   * Or use the NCBI Datasets command‑line tool:

     ```
     datasets download genome accession <GCA_ID> --include genome,annotation
     ```

     This will fetch the sequence and annotation files.

4. **Batch download multiple genomes**

   * If you have a list of many assembly accessions, you can script downloads (e.g. with `wget` or `rsync`) using their FTP paths.
   * The NCBI `assembly_summary.txt` file (for bacteria) provides the mapping from assembly IDs to FTP paths. You can filter for *S. epidermidis* and *complete* level, parse the FTP column, and fetch the files.

5. **Verify completeness / quality**

   * After download, you may run a tool like CheckM, or inspect contig counts, N50, etc. to ensure that the genomes are closed / high quality.

---

If you like, I can run a fresh query right now and list **all current complete *S. epidermidis* genomes** (with accession numbers) and provide you download commands (bash / rsync). Would you like me to do that?

[1]: https://academic.oup.com/database/article/doi/10.1093/database/bau010/2633787?utm_source=chatgpt.com "StaphyloBase: a specialized genomic resource for the staphylococcal research community | Database | Oxford Academic"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5589542/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis ATCC 12228 Chromosome and Plasmids, Generated by Long-Read Sequencing - PMC"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6328648/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis CSF41498 - PMC"
[4]: https://pubmed.ncbi.nlm.nih.gov/28572323/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis 1457 - PubMed"
[5]: https://pubmed.ncbi.nlm.nih.gov/36939347/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis CCSM0287, Isolated from Healthy Facial Skin - PubMed"
[6]: https://pubmed.ncbi.nlm.nih.gov/39791916/?utm_source=chatgpt.com "Complete genome sequence of Staphylococcus epidermidis B273 and its epidermicin NI01 biosynthesis plasmid - PubMed"

I couldn’t find a definitive, up‑to‑date list of *all* *Staphylococcus epidermidis* complete genomes in one place, but here are several confirmed complete (closed) genomes (chromosome + plasmids) from the literature / databases, plus strategies you can use to find the rest.

---

## Examples of confirmed complete *S. epidermidis* genomes

Here are a few strains with published complete genomes:

| Strain / ID                                                                        | Notes / publication                                                 | Accession(s) / details                                                                    |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **ATCC 12228**                                                                     | Long‑read sequenced “complete genome + plasmids”                    | CP022247 to CP022252 ([PMC][1])                                                           |
| **1457**                                                                           | Frequently used in biofilm research; complete genome + plasmid      | CP020462 & CP020463 ([PMC][2])                                                            |
| **CCSM0287**                                                                       | Isolated from healthy facial skin; one chromosome + three plasmids  | As reported in Ma et al. 2023 ([PMC][3])                                                  |
| **RP62A**                                                                          | Methicillin‑resistant strain; in KEGG listed as a “Complete Genome” | Chromosome: CP000029 (plus plasmid pSERP: CP000028) ([KEGG][4])                           |
| **PM221**                                                                          | Isolated from bovine intramammary infection; multiple plasmids      | GCA_000751035.1 (complete) ([KEGG][5])                                                    |
| **14.1.R1**                                                                        | Skin isolate with “exceptional antimicrobial activity”              | One chromosome + plasmids; full genome in PacBio assembly ([PMC][6])                      |
| **ATCC 700577 / ATCC 29887 / ATCC 700566 / ATCC 700570 / ATCC 51625 / ATCC 35547** | Recently published/hybrid assemblies via ATCC genome portal         | Each has downloadable genome & annotation via ATCC portal pages ([ATCC Genome Portal][7]) |

These are examples — the *total count* is likely higher.

---

## 3. How to systematically find all complete genomes and download them

Here’s a workflow (with commands / tips) you can use to enumerate all *complete* *S. epidermidis* genomes in NCBI and fetch them:

1. **Download the bacterial assembly summary table**

   NCBI provides a tabular file `assembly_summary.txt` for bacteria (or for “prokaryotes / RefSeq / GenBank”). For example:

   ```bash
   wget ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt
   # or
   wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/assembly_summary_genbank.txt
   ```

   This file contains metadata for every submitted bacterial assembly: organism name, assembly level (Complete, Scaffold, Contig, etc.), FTP path to files, etc.

2. **Filter for *Staphylococcus epidermidis* + Complete Genome**

   Use `awk` / `grep` / `pandas` etc. For example (bash):

   ```bash
   awk -F "\t" '($8 == "Staphylococcus epidermidis") && ($12 == "Complete Genome") {print}' assembly_summary_genbank.txt > S_epidermidis_complete.txt
   ```

   Here, `$8` is the “organism name” column, `$12` is “assembly level” (or adjust depending on the file’s column layout).

3. **Inspect the filtered list**

   The output lines include (among other fields) the FTP path to the assembly directory. For each such assembly you’ll see something like:

   ```
   ...  ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/xxx/yyy/GCA_xxx_yyy_ASMxxxxxx ...
   ```

4. **Download genome / annotation files**

   Inside each FTP directory, there are files like `*_genomic.fna.gz` (DNA fasta), `*_genomic.gff.gz` (annotation), `*_genomic.gbff.gz` (GenBank flat file), etc.

   Example: for a given FTP directory, you can fetch:

   ```bash
   wget ftp://…/GCA_xxx_yyy_ASMxxxxxx_genomic.fna.gz
   wget ftp://…/GCA_xxx_yyy_ASMxxxxxx_genomic.gff.gz
   wget ftp://…/GCA_xxx_yyy_ASMxxxxxx_assembly_report.txt
   ```

   Or use `rsync` to get all files:

   ```bash
   rsync -av --progress ftp.ncbi.nlm.nih.gov:/genomes/all/GCA/xxx/yyy/GCA_xxx_yyy_ASMxxxxxx/ .
   ```

5. **Use NCBI Datasets CLI (alternate method)**

   NCBI provides a CLI tool `datasets` which you can use to fetch genomes by accession:

   ```bash
   datasets download genome accession GCA_xxx_yyy --include genome,annotation
   ```

   This will download a zip/tarball containing fasta, annotation, etc.

6. **Verify completeness**

   After download, you may want to check:

   * Number of contigs (should be 1 chromosome + plasmids, or very few contigs)
   * N50 / L50
   * CheckM or similar tools to validate completeness / contamination.

---

If you like, I can pull out *all currently listed* complete *S. epidermidis* assemblies (with their FTP paths) from NCBI’s `assembly_summary` and send you a ready-to-use file (or script). Would you like me to prepare that for you?

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5589542/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis ATCC 12228 Chromosome and Plasmids, Generated by Long-Read Sequencing - PMC"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5454206/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis 1457 - PMC"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10112243/?utm_source=chatgpt.com "Complete Genome Sequence of Staphylococcus epidermidis CCSM0287, Isolated from Healthy Facial Skin - PMC"
[4]: https://www.kegg.jp/entry/gn%3AT00229?utm_source=chatgpt.com "KEGG GENOME: Staphylococcus epidermidis RP62A (MRSE)"
[5]: https://www.kegg.jp/entry/gn%3AT03289?utm_source=chatgpt.com "KEGG GENOME: Staphylococcus epidermidis PM221"
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5347227/?utm_source=chatgpt.com "Complete Genome Sequence of a Staphylococcus epidermidis Strain with Exceptional Antimicrobial Activity - PMC"
[7]: https://genomes.atcc.org/genomes/6d52efd69e944bf9?utm_source=chatgpt.com "ATCC® 700577™ | Staphylococcus epidermidis | ATCC Genome Portal"

It looks like I can't run this code right now since you would need to be logged into the Python feature on ChatGPT. But no worries! Here's the script you can use to filter and download the data on your local machine:

### Python Script for Filtering Complete *S. epidermidis* Genomes

```python
import requests

# Download the assembly summary file for bacterial genomes from NCBI FTP
assembly_summary_url = "https://ftp.ncbi.nlm.nih.gov/genomes/all/assembly_summary_genbank.txt"

# Fetch the file content
response = requests.get(assembly_summary_url)
assembly_summary_text = response.text

# Save to a file locally
file_path = "assembly_summary_genbank.txt"
with open(file_path, "w") as file:
    file.write(assembly_summary_text)

# Now, let's filter it for "Staphylococcus epidermidis" and "Complete Genome"
filtered_file_path = "S_epidermidis_complete_genomes.txt"
with open(file_path, "r") as infile:
    lines = infile.readlines()

# Filter lines where "Staphylococcus epidermidis" is mentioned and "Complete Genome" level
with open(filtered_file_path, "w") as outfile:
    for line in lines:
        if "Staphylococcus epidermidis" in line and "Complete Genome" in line:
            outfile.write(line)

print(f"Filtered data saved to: {filtered_file_path}")
```

### Instructions:

1. Install Python on your machine (if not already installed).
2. Save this script as `filter_staph_genomes.py`.
3. Run the script using Python (`python filter_staph_genomes.py`).
4. The script will save a list of complete *S. epidermidis* genomes to a file named `S_epidermidis_complete_genomes.txt`.

This will give you the list of *complete* genomes for *S. epidermidis* and their associated FTP download links. You can then use these to download the genome files.

Let me know if you run into any issues, or if you'd like further assistance with the next steps!

