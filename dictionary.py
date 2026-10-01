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
for j in open(vazn,'r'):
    j=j.strip()
    if j=="":
        continue
    j_part=j.split()
    vazn_j=j_part[0]
    vazn_amino_j=j_part[1]
    vazn_dic[vazn_j]=vazn_amino_j
