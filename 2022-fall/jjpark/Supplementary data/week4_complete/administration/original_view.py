from django.shortcuts import render, redirect
import os
from .forms import UploadFileForm
from django.http import HttpResponse
from collections import defaultdict

# Create your views here.
def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        print(os.getcwd())
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for x in request.FILES.getlist("file"):
                os.system('touch %s/%s' %(os.path.join(os.getcwd(),"media"),x))
                def handle_uploaded_file(f):
                    with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                handle_uploaded_file(x)
            def align(files):
                dicforpair = defaultdict(list)
                dicfornonpair = []
                # paires fastq file QC 
                for f in files:
                    if '.fastq' not in f:
                        continue
                dicforpair['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined

                for k in dicforpair.keys():
                    fqs = ' '.join(dicforpair[k])
                    os.system('/leafeon/analysis1/jjpark/Programs/TrimGalore-0.6.6/trim_galore --path_to_cutadapt /home/jjpark/.local/bin/cutadapt --paired %s' %fqs)
                #hisat genome alignment
                ## indexing
                for f in files:
                    if '.fna' not in f:
                        continue
                    os.system('hisat2-build -p 12 %s queryindex' %f)
                ## align
                new_files = sorted(os.listdir('.'))
                dicforalign = defaultdict(list)
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
                    os.system('hisat2 -p 24 -x queryindex -1 %s 2> %s.log | samtools view -@ 12 -bSF4 | samtools sort -@ 12 - -o %s.bam' %(fqs,k,k))
            listdir = os.listdir(os.path.join(os.getcwd(),"media"))
            align(listdir) 
            context = {'form':form,}
            #return render(request, 'administration/upload.html', context)
            return HttpResponse(" File uploaded! ")
    else:
        form = UploadFileForm()

    return render(request, 'administration/upload.html', {'form': form})

