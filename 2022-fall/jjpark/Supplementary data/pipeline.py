from collections import defaultdict
import os
files = sorted(os.listdir('.'))
dicforpair = defaultdict(list)
dicfornonpair = []
# non pair fastq file QC
'''
for f in files:
    if '.fastq' not in f:
        continue
    dicfornonpair.append(f)
for f in dicfornonpair:
    os.system('//')
# paires fastq file QC 
for f in files:
    if '.fastq' not in f:
        continue
    dicforpair['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined

for k in dicforpair.keys():
    fqs = ' '.join(dicforpair[k])
    os.system('/eevee/val/jjpark/20220916_macrogen_zebrafish/data/TrimGalore-0.6.6/trim_galore --paired %s' %fqs)
#hisat genome alignment
## indexing
for f in files:
    if '.fna' not in f:
        continue
    os.system('/eevee/val/jjpark//hisat2/hisat2-build -p 24 %s queryindex' %f)
'''
## align
new_files = sorted(os.listdir('.'))
dicforalign = defaultdict(list)
## os 확장자 떼고, qc할때 리스트에서 _1_val_1.fq 를 이름으로 붙혀서 사용할수 있음
for f in new_files:
    if '_1_val_1.fq' in f:
        p = f.replace('_1_val_1.fq','')
    elif '_2_val_2.fq' in f: 
        p = f.replace('_2_val_2.fq','')
    else: 
        continue
    dicforalign[p].append(f)

for k in dicforalign.keys():
    fqs = ' -2 '.join(dicforalign[k])
    os.system('/eevee/val/jjpark/hisat2/hisat2 -p 24 -x queryindex -1 %s 2> %s.log | samtools view -@ 24 -bSF4 | samtools sort -@ 24 - -o %s.bam' %(fqs,k,k))
