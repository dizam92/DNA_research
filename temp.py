import os
import pylatex
import glob
from glob import glob

def open_TCGA(path, key_search):
    """ Params:
            path of the directory (for the os.walk)
            key_search gene we want to find
         Return:
             The number of the element if it's there
             If not return 0"""
    os.chdir(path) # cd to the directory
    count = []
    d = {}  # dictionnaire
    for file in glob("*.gene.quantification.txt"): # glob retourne une liste de tous les fichiers qui match ce pattern
        with open("%s" %file, "r") as f:
            ligne = f.readlines()
            for l in ligne:
                l = l[:-1]
                gene, raw_counts, median_length_normalized, RPKM = l.split('\t')
                if gene.find(key_search) != -1:
                    count.append(float(raw_counts))
    return count

if __name__ == '__main__':
    path = "/home/maoss2/PycharmProjects/DNA_research"
    key_search = "DNMT3B"
    count = open_TCGA(path, key_search)
    print count
