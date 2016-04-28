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
    # Can do this for all of the file type and for what i want to find

    # for file in glob("*.gene.quantification.txt"): # glob retourne une liste de tous les fichiers qui match ce pattern
    #     with open("%s" %file, "r") as f:
    #         ligne = f.readlines()
    #         for l in ligne:
    #             l = l[:-1]
    #             gene, raw_counts, median_length_normalized, RPKM = l.split('\t')
    #             if gene.find(key_search) != -1:
    #                 count.append(float(raw_counts))
    for file in glob("*.isoforms.results"): # glob retourne une liste de tous les fichiers qui match ce pattern
        with open("%s" %file, "r") as f:
            ligne = f.readlines()
            for l in ligne:
                l = l[:-1]
                isoform_id, raw_count, scaled_estimate = l.split('\t')
                if isoform_id.find(key_search) != -1:
                    count.append(float(raw_count))

    return count

if __name__ == '__main__':
    #doc = pylatex.Document()
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
                    "/is2/projects/JC_Cancers/TCGA_raw/HNSC/hnsc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/KICH/kich_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/KIRC/kirc_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/KIRC/kirc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/KIRP/kirp_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LIHC/lihc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LUAD/luad_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LUAD/luad_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LUSC/lusc_rnaseq/RNASeq/UNC__IlluminaHiSeq_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/LUSC/lusc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/MESO/meso_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/OV/ov_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/PAAD/paad_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/PCPG/pcpg_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/PRAD/prad_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/READ/read_rnaseq/RNASeq/UNC__IlluminaGA_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/READ/read_rnaseq/RNASeqV2/UNC__IlluminaGA_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/READ/read_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/SARC/sarc_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/SKCM/skcm_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/STAD/stad_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/TGCT/tgct_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/THCA/thca_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/THYM/thym_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/UCEC/ucec_rnaseq/RNASeq/UNC__IlluminaGA_RNASeq/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/UCEC/ucec_rnaseq/RNASeqV2/UNC__IlluminaGA_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/UCEC/ucec_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/UCS/ucs_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3",
                    "/is2/projects/JC_Cancers/TCGA_raw/UVM/uvm_rnaseq/RNASeqV2/UNC__IlluminaHiSeq_RNASeqV2/Level_3"]

    result_file = open("Results.txt", "w")
    for path in list_of_path:
        #, "NM_175849", "NM_175848" , "DNMT3B3", "DNMT3B2", "DNMT3B"
        list_of_keys = ["uc002wyc.3", "uc002wyc.2"]
        d_key_count = {}
        for key in list_of_keys:
            count = open_TCGA(path, key)
            d_key_count[key] = sum(count)

        result_file.write("%s\n" %path)
        result_file.write("------------------------------\n")
        result_file.write("Genes\t Counts\n")
        result_file.write("------------------------------\n")
        for key in list_of_keys:
            result_file.write("%s\t %s\n" % (key, d_key_count[key]))
            result_file.write("------------------------------\n")

    result_file.close()
