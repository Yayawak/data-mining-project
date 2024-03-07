# import streamlit as st 

data = None
def setDataModel(matrix):
    data = matrix

def getData():
    if data is not None:
        return data
    else:
        s = "You must enter data first !!!"
        print(s)
        
        exit(-1)
        # st.write()