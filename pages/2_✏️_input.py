import streamlit as st 
import pandas as pd
from io import StringIO

st.set_page_config(
    page_title = "Input",
    page_icon = "✏️",
)

st.header("Hello World 👏")
st.write("This is my first app")

class LabelWithEditableField:
    def __init__(self, label:str):
        st.write(label)


arr = ["A", "B", "C"]
for a in arr:
    lwe = LabelWithEditableField(a)