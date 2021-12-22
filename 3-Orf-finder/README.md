# Students
강세라/임소연

 * Input: microbial genome sequence (.fna/.fasta nucleotide)
 * Output: All possible open reading frames (.faa amino acids/.coordinate)
 * Options: strandedness/ATG/no-ATG
 * Thinkabouts: i) what is the problem to solve?, ii) why is it important? (biological meaning), iii) how can you design/build/test?how it can be solved?(algorithms/procedures)
 * Example program & literature[^1] - ORFfinder https://www.ncbi.nlm.nih.gov/orffinder/
[^1]: [Borf: Improved ORF prediction in de-novo assembled transcriptome annotation](https://www.biorxiv.org/content/10.1101/2021.04.12.439551v1.full)

# ORF(open reading frame)
https://user-images.githubusercontent.com/91528102/144167591-4ffec221-4c0b-4845-af9e-bc25bf4e99fa.png

https://user-images.githubusercontent.com/91528102/142041888-94b1cc0d-f2f7-474a-a9c5-0669918e0ce6.png

 - ORF란 mRNA로 전사되어 단백질이 될 가능성이 있는, 시작 코돈(일반적으로 AUG)에서부터 종결 코돈(일반적으로 UAA, UAG, UGA)까지의 서열을 말한다.
 - 시작 코돈과 종결 코돈 사이에는 3배수의 염기가 존재하며, 그 이유는 1개의 codon이 3개의 nucleotide에 의해 지정되기 때문이다.
 - 이에 따라 하나의 서열은 6가지 방법(frame)으로 읽을 수 있고 읽는 방법에 따라 6개의 ORF가 존재할 수 있다. (+1, +2, +3, -1, -2, -3 frame)

# why is it important?
 - 단백질로 번역되는 염기 서열을 찾기 위해 모든 DNA 서열을 직접 확인하기에는 시간과 비용이 많이 들기 때문에 ORF를 찾으면 비용적으로나 시간적으로나 효율적이다. 특히 genome size가 클수록 ORF를 찾아서 연구를 진행하는 것이 더 효과적이다.
 - 일반적으로 가능한 ORF 중 가장 긴 ORF를 CDS라고 부르며, CDS는 start codon의 위치, ORF의 길이 등에 의해 결정된다.
 - ORF 연구를 통해 병원체가 어떤 단백질을 생산하는지 알아낸다면 병원체의 작동 원리를 파악할 수 있고, 때문에 ORF 연구는 치료제와 백신 연구에 중요하다.
 
# algorithms
https://user-images.githubusercontent.com/91528102/146112346-113b2c40-063a-44c2-b2e5-531f4e68ccdf.png

# Option
 - choose codon table
 - minimum ORF length
 - ORF length distribution

# ORF program
 
 - https://www.bioinformatics.org/sms2/orf_find.html
 - https://sites.google.com/site/dwivediplanet/ORF-Investigator
 - https://bioinformatics.ysu.edu/tools/OrfPredictor.html
 - https://www.ncbi.nlm.nih.gov/orffinder/
 - https://github.com/betsig/borf
 - https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1

# Benchmark
https://user-images.githubusercontent.com/91528102/146115168-617f9813-a60a-41cb-81cf-5cb4bd3cc23b.png
