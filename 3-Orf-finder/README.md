# Students
강세라/임소연

 * Input: microbial genome sequence (.fna/.fasta nucleotide)
 * Output: All possible open reading frames (.faa amino acids/.coordinate)
 * Options: strandedness/ATG/no-ATG
 * Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?how it can be solved?(algorithms/procedures)
 * Example program & literature[^1] - ORFfinder https://www.ncbi.nlm.nih.gov/orffinder/
[^1]: [Borf: Improved ORF prediction in de-novo assembled transcriptome annotation](https://www.biorxiv.org/content/10.1101/2021.04.12.439551v1.full)

# ORF

![image](https://user-images.githubusercontent.com/91528102/142041888-94b1cc0d-f2f7-474a-a9c5-0669918e0ce6.png)

![image](https://user-images.githubusercontent.com/91528102/140896095-954a19e3-e637-4a8a-86dc-3174df088a82.png)
 - mRNA로 전사되어 단백질이 될 가능성이 있는 염기 서열.
 - 시작 코돈(AUG)에서부터 종결 코돈(UAA, UAG, UGA)까지의 서열.
 - ATG-[3n]-TAG와 같이 시작 코돈과 종결 코돈 사이에 3배수의 염기가 존재.

# why is it important?
 - 단백질로 번역되는 염기 서열을 찾기 위해 모든 DNA 서열을 직접 확인하기에는 시간과 비용이 많이 들기 때문에 ORF를 찾으면 더 쉽게 원하는 서열을 찾을 수 있다.

# algorithms
![image](https://user-images.githubusercontent.com/91528102/142042011-4999c081-6da9-4cad-83c1-c3a0f985c040.png)

# python code
http://localhost:8888/notebooks/ORF%20finder.ipynb

# option
 - 원하는 strand input(+1, +2, +3, -1, -2, -3 중에 선택)
 - ORF length distribution
 - alternative start/stop codon

# ORF program
 
 - https://www.bioinformatics.org/sms2/orf_find.html
 - https://sites.google.com/site/dwivediplanet/ORF-Investigator
 - https://bioinformatics.ysu.edu/tools/OrfPredictor.html
 - https://www.ncbi.nlm.nih.gov/orffinder/
 - https://github.com/betsig/borf
