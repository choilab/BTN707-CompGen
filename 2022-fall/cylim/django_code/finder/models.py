from django.db import models
import os
from datetime import datetime
import time

class speDB(models.Model):
    Data_choices = (
    ("human", "human"),
    ("ecoli", "E. coli"),
    ("yeast", "S. cerevisiae"),
)
    species = models.CharField(
        max_length = 30,
        choices = Data_choices,
        default = 'human'
        )

def handle_uploaded_file(f):
    with open(os.path.join(os.getcwd(),'media',f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def running(g):
    x = str(datetime.now()).replace(" ","_").replace(".","_")
    os.system("mkdir output/{}".format(x))
    DB = "/panpyro/alfa/cylim/foldseek/DB/Alphafold/modelorg/speciesdb/ecolidb"
    time.sleep(1)
    os.system("foldseek easy-search media/{} {} output/aln output/tmp".format(g,DB))
    #for i in range(0,l):



#os.system("foldseek easy-search ../input/AF-A0A385XJ53-F1-model_v4.pdb /panpyro/alfa/cylim/foldseek/DB/Alphafold/modelorg/speciesdb/ecolidb ../output/aln ../output/tmp")


# Create your models here.
