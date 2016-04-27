__author__ = 'maoss2'
# -*- coding: utf-8 -*-
import os
import pylatex
import glob

def open_TCGA(path, key_search):
    """ Params:
            path of the directory (for the os.walk)
            key_search gene we want to find
         Return:
             The number of the element if it's there
             If not return 0"""
    count = []
    for racine, repertoire, file in os.walk(path):
        for f in file:
            d = {}  # dictionnaire
            with open(f, "r") as f:
                ligne = f.readline()  # lecture de chaque ligne
                while ligne != '':
                    if ligne == '\n':
                        ligne = f.readline()
                        continue
                    ligne = ligne[:-1]
                    valeur1, valeur2 = ligne.split('\t')
                    d[valeur1] = float(valeur2)
                    ligne = f.readline()
            if key_search in d:
                count.append(d[key_search])
            else:
                count.append(0)
        return count

if __name__ == '__main__':
    doc = pylatex.Document()
    os.chdir('/is2/projects/JC_Cancers/TCGA_raw/BRCA/brca_rnaseq.final')
    path = "/is2/projects/JC_Cancers/TCGA_raw/BRCA/brca_rnaseq.final"
    #, "DNMT3B", "DNMT3B2", "NM_175849", "NM_175848"
    list_of_keys = ["uc002wyc.3", "uc002wyc.2"]
    d_key_count = {}
    for key in list_of_keys:
        count = open_TCGA(path, key)
        d_key_count[key] = sum(count)

    with doc.create(pylatex.Section("BRCA Cancer")):
        with doc.create(pylatex.Subsection("%s\n" %path)):
            doc.pylatex.append("%s\n" % list_of_keys[0])
            with doc.create(pylatex.Tabular('|r||l|')) as table:
                table.add_hline()
                table.add_row(("Genes", 'Counts'))
                table.add_hline()
                table.add_row(("%s" % list_of_keys[0], d_key_count[list_of_keys[0]]))
                table.add_hline()
                table.add_row(("%s" % list_of_keys[1], d_key_count[list_of_keys[1]]))
                table.add_hline()

    #redo the search for all the file
    doc.generate_pdf('Count_Results')

    print d_key_count