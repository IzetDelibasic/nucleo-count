import pandas as pd
import streamlit as st 
import altair as alt  
from PIL import Image

image = Image.open("nucleotideImage.webp")

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Counter

DNA Counter counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
         ***
         """)

st.header('OUTPUT (DNA Nucleotide Count)')
def DNA_nucletiode_count(seq):
    d=dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X= DNA_nucletiode_count(sequence)

X


