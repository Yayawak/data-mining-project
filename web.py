import streamlit as st 

st.header("Hello World 👏")
st.write("This is my first app")

dataset_name = "Breast cancel"
csv_file = st.file_uploader(f"upload you {dataset_name} file.csv ", ['.csv'])