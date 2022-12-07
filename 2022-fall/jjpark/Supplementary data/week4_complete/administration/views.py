from django.shortcuts import render, redirect
import os
from .forms import UploadFileForm
from django.http import HttpResponse
from collections import defaultdict

# Create your views here.
def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for x in request.FILES.getlist("file"):
                os.system('touch %s/%s' %(os.path.join(os.getcwd(),"media"),x))
                def handle_uploaded_file(f):
                    with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                handle_uploaded_file(x)
            files = os.listdir(os.path.join(os.getcwd(),"media"))
            root = os.path.join(os.getcwd(),"media")+'/'
            dicforpair = defaultdict(list)
            # paires fastq file QC 
            for f in files:
                if '.fastq' not in f and '.txt' in f:
                    continue
                dicforpair['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined
            for k in dicforpair.keys():
                fqs = '//_///'.join(dicforpair[k])
                fqs = fqs.replace('//_///',' '+root)
                os.system('/leafeon/analysis1/jjpark/Programs/TrimGalore-0.6.6/trim_galore --path_to_cutadapt /home/jjpark/.local/bin/cutadapt -o %s --paired %s%s' %(root,root,fqs))           
            #hisat genome alignment
            '''
            ## indexing
            for f in files:
                if '.fna' not in f:
                    continue
                os.system('hisat2-build -p 12 %s%s %squeryindex' %(root,f,root))
            ##################complete##############
            '''
            ## align
            new_files = sorted(os.listdir('/leafeon/analysis1/jjpark/practice_django/week4_try2/media')) #Change os.path.join
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
                fqs = '//////_/////'.join(dicforalign[k])
                fqs = fqs.replace('//////_/////',' -2 '+root)
                os.system('hisat2 -p 12 -x %squeryindex -1 %s%s 2> %s%s.log | samtools view -@ 12 -bSF4 | samtools sort -@ 12 - -o %s%s.bam' %(root,root,fqs,root,k,root,k)) 
            context = {'form':form,}
            #return render(request, 'administration/upload.html', context)
            return HttpResponse(" File uploaded! ")
    else:
        form = UploadFileForm()

    return render(request, 'administration/upload.html', {'form': form})

