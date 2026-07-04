from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_rna_by_name["Standard"]
#print(standard_table.forward_table["AUG"])
def translate_rna_sequence(rna_sequence):
    standard_table = CodonTable.unambiguous_rna_by_name["Standard"]

    rna = rna_sequence.upper().strip()
    if not all(base in "AUGC" for base in rna):
        print("Error: Invalid character found. RNA must only contain A, U, G, C")

    protein_chain = []
    print(f"\nAnalyzing RNA Sequence: {rna}")
    for i in range(00, len(rna)- 2, 3):
        codon = rna [i:i+3]

        if codon in standard_table.stop_codons:
            print(f"Found STOP codon ({codon}). Translate terminated.")
            break
        amino_acid = standard_table.forward_table.get(codon, '?')
        protein_chain.append(amino_acid)
    final_protein = "-".join(protein_chain)
    print(f"Final Protein Chain: {final_protein}\n")
    return final_protein


user_dna = input("ENTER YOUR DNA SEQUENCE : ")
user_rna = user_dna.upper().replace("T", "U")
translate_rna_sequence(user_rna)