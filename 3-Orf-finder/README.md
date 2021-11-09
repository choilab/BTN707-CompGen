# Students
강세라/임소연

# Open Reading Frame (ORF) finder

Input: microbial genome sequence (.fna/.fasta nucleotide)

Output: All possible open reading frames (.faa amino acids/.coordinate)

Options: strandedness/ATG/no-ATG

Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?...

Example program & literature3 - ORFfinder https://www.ncbi.nlm.nih.gov/orffinder/

Borf: Improved ORF prediction in de-novo assembled transcriptome annotation

# ORF

 - 시작 코돈(AUG)에서부터 종결 코돈(UAA, UAG, UGA)까지의 서열.
 - ATG-[3n]-TAG와 같이 시작 코돈과 종결 코돈 사이에 3배수의 염기가 존재.

ORF program
 
 - https://www.bioinformatics.org/sms2/orf_find.html
 - https://sites.google.com/site/dwivediplanet/ORF-Investigator
 - https://bioinformatics.ysu.edu/tools/OrfPredictor.html
 - https://www.ncbi.nlm.nih.gov/orffinder/
