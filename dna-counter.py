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