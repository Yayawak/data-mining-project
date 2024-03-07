import streamlit as st 
import pandas as pd

st.set_page_config(
    page_title = "Upload",
    page_icon = "📩",
)

dataset_name = "Breast cancel"

uploaded_file = st.file_uploader(f"upload you {dataset_name} file.csv ", ['.csv'])
if (uploaded_file is not None):
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    print(dataframe)
    # st.write(dataframe)
