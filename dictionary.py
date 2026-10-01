import os 



codon = os.path.join(r"D:\quera\BioForge-main\data", "codon_table.txt")



conon_dic= {}

for i in open(codon, "r"):
    i=i.strip()
    if i == "":
        continue
    i_parts=i.split()
    codon_i=i_parts[0]
    amino_i=i_parts[1]
    conon_dic[codon_i] = amino_i


vazn = os.path.join(r"D:\quera\BioForge-main\data", "codon_weoghts.txt")


vazn_dic={}
<<<<<<< HEAD
for j in open(vazn,'r'):
=======
for j in open(vazn,"r"):
>>>>>>> 804e7a9835a9a333202dad69878690f8b88fadb2
    j=j.strip()
    if j=="":
        continue
    j_part=j.split()
    vazn_j=j_part[0]
    vazn_amino_j=j_part[1]
    vazn_dic[vazn_j]=vazn_amino_j
