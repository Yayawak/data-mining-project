import streamlit as st


st.set_page_config(
    page_title = "Welcome",
    page_icon = "🏠",
)

st.title("Hello This is Breast Cancer Diagnosis Prediction ")
st.sidebar.success("select page above")

st.image('breastcancer.png', caption='')