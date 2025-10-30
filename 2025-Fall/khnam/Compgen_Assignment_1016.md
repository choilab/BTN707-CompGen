# Genome (*Staphylococcus epidermidis*) identified on NCBI database

All the contents in column are cited from the NCBI database

| All Genome | Annotated |
|:----------:|:---------:|
|  5316      |   5038    |

In annotated genomes, there are categorized by assembly level.

| Complete | Chromosome | Scaffold | Contig |
|:--------:|:----------:|:--------:|:------:|
|   5038   |   4755     |    4719  |  3316  |

# Assignments performed on class
## Q1. How many genomes have been published for *Staphylococcus epidermidis*?

Based on NCBI data, approximately 5038 annotated genomes of *S.epidermidis* are available at complete genome level
Selecting the lower assembly level (e.g. chromosome, scaffold), the number of genomes available decreases

## Q2. Then, how can they be downloaded?

1. Connect to [NCBI Assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/)
2. Search *Staphylococcus epidermidis*
3. Set filter : Assembly level = Complete genome
4. Choose the strain you want
5. Download genome -> format: .fna (genome sequence), .gff (annotation features) 

The 272 Refseq genomes of *S.epidermidis* are downloaded

# Genome Selection Project: ANI-based Filtering (272 -> 124 genomes)

**Project Goal:** To filter a set of 272 genomes based on Average Nucleotide Identity (ANI) to remove duplicates or highly similar strains, resulting in a representative set of 124 genomes.

---

## 1. Analysis Environment Setup

All analyses were performed in a Conda virtual environment.

### 1-1. Create and Activate Conda Environment

Create an environment named `ani_env` with `fastani` installed.

```bash
# Create Conda environment
conda create -n ani_env fastani -c bioconda

# Activate environment
conda activate ani_env
```

### 1-2. Prepare Input Files

All 272 genome FASTA files must be located in a single directory.

* **Genome Directory:** `./All_272_Genomes/` (Example path)
* **File Extension:** `.fna` (or `.fa`, `.fasta`, etc.)

---

## 2. Running FastANI

Use `fastani` to perform an all-versus-all ANI comparison among the 272 genomes.

### 2-1. Create Genome List

`fastani` requires a text file listing the paths to all input genomes.

```bash
# Find all .fna files in the directory and save the list to genome_list.txt
find ./All_272_Genomes/ -name "*.fna" > genome_list.txt
```

### 2-2. Execute ANI Calculation

Run `fastani` using the `genome_list.txt` file for both query and reference.

* `--ql`: `genome_list.txt` (Query list)
* `--rl`: `genome_list.txt` (Reference list)
* `-o`: `ani_results.tsv` (Output file name)
* `-t`: 8 (Number of threads to use; adjust based on your system)

```bash
fastani --ql genome_list.txt --rl genome_list.txt -o ani_results.tsv -t 8
```

>
> ```bash
> nohup fastani --ql genome_list.txt --rl genome_list.txt -o ani_results.tsv -t 8 &
> ```

---

## 3. Result Parsing and Genome Filtering (Python)

The output file (`ani_results.tsv`) contains the pairwise ANI values. We will use a Python script (with Pandas) to parse this file, cluster genomes above a threshold (e.g., 99%), and select one representative from each cluster.

> **Logic:** This script groups genomes with >= 99% ANI as 'the same' and adds one of them to a removal list.

```python
import pandas as pd

# 1. Load the ANI results file
# FastANI output has no header; provide column names
ani_df = pd.read_csv(
    "ani_results.tsv",
    sep='\t',
    header=None,
    names=["Query", "Reference", "ANI", "Mappings", "Total_Fragments"]
)

# 2. Set the filtering threshold (e.g., 99%)
THRESHOLD = 99.0

# 3. Find pairs above the threshold (excluding self-comparisons)
similar_pairs = ani_df[
    (ani_df['ANI'] >= THRESHOLD) & 
    (ani_df['Query'] != ani_df['Reference'])
]

# 4. Deduplication logic
# (Simple logic: if a genome is in the remove list, skip it)
genomes_to_remove = set()
genomes_to_keep = set(ani_df['Query'].unique()) # Start by assuming we keep all genomes

for index, row in similar_pairs.iterrows():
    query_genome = row['Query']
    ref_genome = row['Reference']

    # If neither genome is already set for removal, add one
    if (query_genome not in genomes_to_remove) and (ref_genome not in genomes_to_remove):
        # Here, we simply remove the 'Reference' (other criteria could be used)
        genomes_to_remove.add(ref_genome)

# 5. Get the final set of genomes to keep
final_genomes_to_keep = genomes_to_keep - genomes_to_remove

print(f"Initial genome count: {len(genomes_to_keep)}")
print(f"Genomes to remove: {len(genomes_to_remove)}")
print(f"Final representative genome count: {len(final_genomes_to_keep)}")

# 6. Save the final list to a file
with open("final_124_genome_list.txt", "w") as f:
    for genome_path in final_genomes_to_keep:
        f.write(genome_path + "\n")

print("Final genome list saved to 'final_124_genome_list.txt'")
```

---

## 4. Copy Representative Genome Files

Finally, copy the 124 selected genome FASTA files from the original directory into a new directory (`Rep_genomes/`).

```bash
# Create the new directory for representative genomes
mkdir Rep_genomes

# Read the list file line by line and copy the files
while read -r genome_path; do
    cp "$genome_path" ./Rep_genomes/
done < final_124_genome_list.txt

echo "Copying of 124 representative genomes complete."
```
