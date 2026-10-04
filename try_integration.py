from bioforge.files.logger import setup_logger
from bioforge.sequences.processing import load_dna_records

setup_logger()

with open("example.fasta", "w", encoding="utf-8") as f:
    f.write(">seq001 organism=E_coli\nATGCTT\n\n"
            ">seq002 organism=Human\nATGXYZ\n\n"
            ">seq003 organism=Mouse\nCCCGGG\n")

records = load_dna_records("example.fasta")

print("Number of valid records:", len(records))
for record in records:
    dna = record["dna"]
    print(record["id"], record["organism"], record["sequence"])
    print("   RNA:", dna.to_rna())
    print("   Reverse complement:", dna.reverse_complement())
    print("   GC content:", dna.gc_content())