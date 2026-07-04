import streamlit as st
from Bio.Seq import Seq

st.title("DNA to Protein translation pipeline🧬")
st.write("Enter a DNA sequence below to translate it into Protein chain")

user_input = st.text_input("Enter the DNA sequence :", "").upper()

if st.button("Translate Sequence"):
    if user_input:
        if any(char not in "ATGC" for char in user_input):
            st.error("Invalid Sequence! Please enter only A, T, G, or C letters.")
        else:
            dna_seq = Seq(user_input)
            rna_seq = dna_seq.transcribe()

            st.subheader("Results: ")
            st.info(f"**Transcribed RNA:** {rna_seq}")

            protein_seq = rna_seq.translate(to_stop=True)
            st.success(f"**Final Protein Chain:** {protein_seq}")

    else:
        st.warning("Please enter a sequence first!")