from math import ceil
from typing import List
from shiny import App, render, ui
import os
from collections import defaultdict

dicforpair = defaultdict(list)
dicforalign = defaultdict(list)
os.system('mkdir media')
root = os.path.join(os.getcwd(),"media")+'/'

def ui_card(title, *args):
    return (
        ui.div(
            {"class": "card mb-4"},
            ui.div(title, class_="card-header"),
            ui.div({"class": "card-body"}, *args),
        ),
    )



app_ui = ui.page_fluid(
        ui.input_file("file1", "Choose a file to upload:", multiple=True),
        ui.output_text_verbatim("file_content"),
        ui_card("Download",ui.download_button("download1","Download"))
)


def server(input, output, session):
        @output
        @render.text
        #@output
        def file_content():
            file_infos = input.file1()
            if not file_infos:
                return
                # file_infos is a list of dicts; each dict represents one file. Example:
                # [
                #   {
                #        'name': 'data.csv',
                #        'size': 2601,
                #        'type': 'text/csv',
                #        'datapath': '/tmp/fileupload-1wnx_7c2/tmpga4x9mps/0.csv'
                #   }
                # ]
            #Write
            for file_info in file_infos:
                file_name = file_info["name"]
                with open (file_info["datapath"], "r") as f:
                    with open('%s%s' %(root,file_name), 'w') as g:
                        for line in f.readlines():
                            g.write(line)
            #Trim_galore
            files = os.listdir(root)
            for f in files:
                if '.fastq' not in f and '.txt' in f:
                    continue
                dicforpair['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined
                for k in dicforpair.keys():
                    fqs = '//_///'.join(dicforpair[k])
                    fqs = fqs.replace('//_///',' '+root)
                    os.system('/leafeon/analysis1/jjpark/Programs/TrimGalore-0.6.6/trim_galore --path_to_cutadapt /home/jjpark/.local/bin/cutadapt -o %s --paired %s%s' %(root,root,fqs))
            #Indexing
            for f in files:
                if '.fna' not in f:
                    continue
                os.system('hisat2-build -p 12 %s%s %squeryindex' %(root,f,root))
            new_files = os.listdir(root)
            #Align
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
            
            # Upload & Pipeline completed.
            out_str = 'Upload & Align complete'
            return out_str
        
        #Download
        @session.download()
        def download1():
            output_files = os.listdir(root)
            for bam in output_files:
                if '.bam' not in bam:
                    continue
                path = root +'/'+ bam
            return path                                #return require path/filename of qurey file


app = App(app_ui, server)
