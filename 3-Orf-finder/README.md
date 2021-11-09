# Students
강세라/임소연

 * Input: microbial genome sequence (.fna/.fasta nucleotide)
 * Output: All possible open reading frames (.faa amino acids/.coordinate)
 * Options: strandedness/ATG/no-ATG
 * Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?...
 * Example program & literature[^1] - ORFfinder https://www.ncbi.nlm.nih.gov/orffinder/
[^1]: [Borf: Improved ORF prediction in de-novo assembled transcriptome annotation](https://www.biorxiv.org/content/10.1101/2021.04.12.439551v1.full)

# ORF

 - mRNA로 전사되어 단백질이 될 가능성이 있는 염기 서열.
 - 시작 코돈(AUG)에서부터 종결 코돈(UAA, UAG, UGA)까지의 서열.
 - ATG-[3n]-TAG와 같이 시작 코돈과 종결 코돈 사이에 3배수의 염기가 존재.
 - ORF(open reading frame)가 반드시 단백질로 번역되는 것을 의미하지는 않는다. 실제로 세포 안에서 단백질로 번역되는지는 실험적으로 확인해야 하지만 모든 DNA 단편을 직접 확인하기에는 많은 시간과 비용이 발생하므로, DNA 서열상에서 ORF(open reading frame)을 예측하기 위한 다양한 프로그램들이 개발되었다.

ORF program
 
 - https://www.bioinformatics.org/sms2/orf_find.html
 - https://sites.google.com/site/dwivediplanet/ORF-Investigator
 - https://bioinformatics.ysu.edu/tools/OrfPredictor.html
 - https://www.ncbi.nlm.nih.gov/orffinder/
