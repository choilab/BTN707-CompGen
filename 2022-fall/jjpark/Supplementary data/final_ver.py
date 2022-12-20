from math import ceil
from typing import List
from shiny import App, render, ui
import os
from collections import defaultdict
from datetime import datetime

dicforpair = defaultdict(list)
dicforalign = defaultdict(list)
dicforvalidity = defaultdict(list)
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
    ui.tags.style(
        """
        .app-col {
            border: 1px solid black;
            border-radius: 5px;
            background-color: #eee;
            padding: 8px;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        """
    ),
    ui.h2({"style": "text-align: center;"}, "OCRWA(One-Click RNA-seq pipeline Web App)"),
    ui.row(
        ui.column(
            12,
            ui.div(
                {"class": "app-col"},
                """
                After you get raw FASTQ files after NGS(Next-Generation Sequencing), you have to go through computational processes such as adapter trimming, quality control, alignment to proceed with the follow-up study.
                We provide a one-click web app for the above process. 
                After uploading the fastq file and reference genome, you can get the BAM files and gene count tables that are available for the study immediately.
                Please refer to NOTICE below and use our web app service.
                """,
            ),
        ),
    ),
    ui.row(
        ui.column(
            12,
            ui.div(
                {"class": "app-col"},
                ui.p(
                    """
                    NOTICE
                    """,
                ),
                ui.p(
                    """
                    - You need to upload query FASTQ files, reference genome's FNA, GTF files to align & counting reads. If you do not upload the required files, please check error message and upload files agian.
                    """,
                ),
                ui.p(
                    """
                    - Upload paired-FASTQ files to sample_1.fastq & sample_2.fastq. The same paired-samples must be grouped by _1 and _2. We do not serve for single-end FASTQ yet.
                    """,
                ),
                ui.p(
                    """
                    - If your research's reference genome is one of the option below, please choose one. You don't need to upload FNA or GTF files. Also it significantly reduces running time.
                    """,
                ),
                ui.p(
                    """
                    - You can get BAM file, gene count table, alignment log as a result of one-click. Please unzip tar and use it
                    """,
                ),
            ),
        )
    ),
    ui.input_radio_buttons(
        "modelanimal", "If your data is one of the options below, choose for fast processing", {"human" : "Homo sapiens","mouse" : "Mus musculus","zebrafish" : "Danio rerio", "else" : "None" }
    ),
    ui.input_file("file1", "Choose a file to upload:", multiple=True),
    ui.output_text_verbatim("process"),
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
            
            check = os.listdir(root)
            #MODEL = NONE
            if input.modelanimal() == 'else':
                #Validity Check
                fna = 0
                gtf = 0
                for i in check:
                    if '.fna' in i:
                        fna += 1
                if fna != 1:
                    return "ERROR : Please verify that one fna file exists"

                for i in check:
                    if '.gtf' in i and '_____306' not in i:
                        gtf += 1
                if gtf != 1:
                    return "ERROR : Please verify that one gff file exists"

                for f in check:
                    if '.fastq' not in f or  '.txt' in f:
                        continue
                    dicforvalidity['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined
                for k in dicforvalidity.keys():
                    if len(dicforvalidity[k]) != 2:
                        return "ERROR : Please verify that the paired fastq files are named id_1, id_2"
                #Trim_galore
                files = os.listdir(root)
                for f in files:
                    if '.fastq' not in f or  '.txt' in f:
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
                    elif '_2_val_1.fq' in f:
                        p = f.replace('_2_val_1.fq','')
                    elif '_1_val_2.fq' in f:
                        p = f.replace('_1_val_2.fq','')

                    else:
                        continue
                    dicforalign[p].append(f)
                for k in dicforalign.keys():
                    fqs = '//////_/////'.join(dicforalign[k])
                    fqs = fqs.replace('//////_/////',' -2 '+root)
                    os.system('hisat2 -p 12 -x %squeryindex -1 %s%s 2> %s%s.log | samtools view -@ 12 -bSF4 | samtools sort -@ 12 - -o %s%s.bam' %(root,root,fqs,root,k,root,k))
                #FeatureCounts
                bams = os.listdir(root)
                gtf = ''.join([i for i in bams if '.gtf' in i and '_____306' not in i])
                bam = [i for i in bams if '.bam' in i]
                ba = '///////////_////////'.join(bam)
                ba = ba.replace('///////////_////////',' %s' %root)
                os.system('featureCounts -T 12 -a %s/%s -o %s/count_table.tsv %s%s' %(root,gtf,root,root,ba))

                # Upload & Pipeline completed.
                out_str = 'Success! All Process Complete'
                return out_str
            #MODELANIMAL handling
            else:
                model = input.modelanimal()
                #Validity Check
                for f in check:
                    if '.fastq' not in f or  '.txt' in f:
                        continue
                    dicforvalidity['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined
                for k in dicforvalidity.keys():
                    if len(dicforvalidity[k]) != 2:
                        return "ERROR : Please verify that the paired fastq files are named id_1, id_2"
                #Trim_galore
                files = os.listdir(root)
                for f in files:
                    if '.fastq' not in f or  '.txt' in f:
                        continue
                    dicforpair['_'.join(f.split('_')[:-1])].append(f) #In dicforfair, alfa_1 & alfa_2 combined
                for k in dicforpair.keys():
                    fqs = '//_///'.join(dicforpair[k])
                    fqs = fqs.replace('//_///',' '+root)
                    os.system('/leafeon/analysis1/jjpark/Programs/TrimGalore-0.6.6/trim_galore --path_to_cutadapt /home/jjpark/.local/bin/cutadapt -o %s --paired %s%s' %(root,root,fqs))
                #Indexing pass
                new_files = os.listdir(root)
                for f in new_files:
                    if '_1_val_1.fq' in f:
                        p = f.replace('_1_val_1.fq','')
                    elif '_2_val_2.fq' in f:
                        p = f.replace('_2_val_2.fq','')
                    elif '_2_val_1.fq' in f:
                        p = f.replace('_2_val_1.fq','')
                    elif '_1_val_2.fq' in f:
                        p = f.replace('_1_val_2.fq','')
                    else:
                        continue
                    dicforalign[p].append(f)
                for k in dicforalign.keys():
                    fqs = '//////_/////'.join(dicforalign[k])
                    fqs = fqs.replace('//////_/////',' -2 '+root)
                    os.system('hisat2 -p 12 -x %s%s -1 %s%s 2> %s%s.log | samtools view -@ 12 -bSF4 | samtools sort -@ 12 - -o %s%s.bam' %(root,model,root,fqs,root,k,root,k))
                #FeatureCounts
                bams = os.listdir(root)
                gff = model +'_____306.gtf'
                bam = [i for i in bams if '.bam' in i]
                ba = '///////////_////////'.join(bam)
                ba = ba.replace('///////////_////////',' %s' %root)
                os.system('featureCounts -T 12 -a %s/%s -o %s/count_table.tsv %s%s' %(root,gff,root,root,ba))
                # Upload & Pipeline completed.
                out_str = 'Success! All Process Complete'
                return out_str
        #Download
        @session.download()
        def download1():
            os.chdir(root)
            with open ('%s/count_table.tsv' %root) as f1:
                with open ('%s/simple_count_table.tsv' %root , 'w') as g1:
                    lines = f1.readlines()
                    for line in lines[1:]:
                        gid = line.split('\t')[0]
                        counts = '\t'.join(line.split('\t')[6:])
                        counts = counts.replace(root,'')
                        g1.write(gid+'\t'+counts)
            output_files = os.listdir(root)
            downloadfiles = [i for i in output_files if '.bam' in i or 'count_table.tsv' in i]
            dofo = ' '.join(downloadfiles)
            os.system('tar -cvf output.tar %s' %dofo)
            path = root+'output.tar'
            os.chdir('../')
            return path                                #return require path/filename of qurey filei


app = App(app_ui, server)

