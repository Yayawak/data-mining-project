import pandas as pd
import numpy as np
import streamlit as st 

st.set_page_config(
    page_title = "Upload",
    page_icon = "📩",
)

dataset_name = "Breast cancel"

def onSubmit(numpy_array):
    ...
    print(numpy_array.shape)

uploaded_file = st.file_uploader(f"upload you {dataset_name} file.csv ", ['.csv'])
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    dataframe = pd.read_csv(uploaded_file)
    dataframe.drop(columns=['id'], inplace=True)
    numpy_array = dataframe.values

    st.write(dataframe)
    # st.write(numpy_array)
    st.button("Predict", key="predict button", on_click=onSubmit(numpy_array), type="primary")