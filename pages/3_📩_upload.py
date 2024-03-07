import pandas as pd
import numpy as np
import streamlit as st 
from model import loadModel
from joblib import load
from decoder import decode
model = loadModel() 

st.set_page_config(
    page_title = "Upload",
    page_icon = "📩",
)

dataset_name = "Breast cancel"

numpy_array = None 
def onSubmit():
    global numpy_array
    print(numpy_array.shape)
    sc= load('std_scaler.bin')
    X_test_std = sc.transform(numpy_array)
    pred = model.predict(X_test_std)

    for p in pred:
        st.subheader(f"Result is {decode(p)}")
    print(pred)


uploaded_file = st.file_uploader(f"upload you {dataset_name} file.csv ", ['.csv'])
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    dataframe = pd.read_csv(uploaded_file)
    # dataframe.drop(columns=['id'], inplace=True)
    numpy_array = dataframe.values

    st.write(dataframe)
    # st.write(numpy_array)
    st.button("Predict", key="predict button", on_click=onSubmit, type="primary")
    # st.button("Predict", key="predict button", on_click=lambda : onSubmit(numpy_array), type="primary")
