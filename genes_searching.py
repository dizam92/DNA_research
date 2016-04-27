__author__ = 'maoss2'
# -*- coding: utf-8 -*-
import os
import pylatex
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
    doc = pylatex.Document()
    list_of_path = ["/is2/projects/JC_Cancers/TCGA_raw/BRCA/brca_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/BRCA/brca_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/BLCA/blca_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/BLCA/blca_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LAML/laml_rnaseq/RNASeq/BCGSC__IlluminaGA_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LAML/laml_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LGG/lgg_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/ACC/acc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/CESC/cesc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/CHOL/chol_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/COAD/coad_rnaseq/RNASeq/UNC__IlluminaGA_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/COAD/coad_rnaseq/RNASeqV2/UNC__IlluminaGA_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/COAD/coad_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/DLBC/dlbc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/ESCA/esca_rnaseq/RNASeq/BCGSC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/ESCA/esca_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/FPPP/fppp_rnaseq/TotalRNASeqV2/UNC__IlluminaHiSeq_TotalRNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/GBM/gbm_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/HNSC/hnsc_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/HNSC/hnsc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3"]
    for path in list_of_path:
        #, "NM_175849", "NM_175848"
        list_of_keys = ["uc002wyc.3", "uc002wyc.2", "DNMT3B3", "DNMT3B2", "DNMT3B"]
        d_key_count = {}
        for key in list_of_keys:
            count = open_TCGA(path, key)
            d_key_count[key] = sum(count)
            # with doc.create(pylatex.Section("BRCA Cancer")):

        with doc.create(pylatex.Section("%s\n" %path)):
            with doc.create(pylatex.Tabular('|r|l|')) as table:
                table.add_hline()
                table.add_row(("Genes", 'Counts'))
                table.add_hline()
                for key in list_of_keys:
                    table.add_row(("%s" % key, d_key_count[key]))
                    table.add_hline()

    doc.generate_pdf('Count_Results')
