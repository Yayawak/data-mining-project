import streamlit as st 
import pandas as pd
from io import StringIO
import numpy as np
from model import loadModel
from joblib import load
from decoder import decode
model = loadModel()

st.set_page_config(
    page_title = "Input",
    page_icon = "✏️",
)

st.header("Enter Your Data before Prediction ☺️")
# st.write("This is my first app")

class LabelWithEditableField:
    def __init__(self, label:str):
        
        self._number = 0
        # st.write(label) 
        # self.tinput = st.text_input(label, key=label, on_change=self.search_callback)
        search_str = st.text_input(label, key=label, placeholder=f'enter {label}',
            on_change=self.search_callback, args=[label,], value=self._number)

    # def getValue(self) -> str:
    #     return self.tinput
    def validateOnlyNumber(self, s:str) -> bool:
        try:
            number = float(s)
            return True
        except Exception as e:
            print(f'Cannot convert {s} string to float\n')
            return False

    def getValue(self):
        return self._number

    def search_callback(self, *args, **kwargs):
        # print(args)
        input_txt = st.session_state[args[0]]
        if (self.validateOnlyNumber(input_txt)):
            # print(float(input_txt))
            self._number = float(input_txt)

            getAllColumnData()
        else:
            st.write(f"You must input numerical attribute for {args[0]}") 


        print(f"{args[0]} with {input_txt}")

        # st.write("You searched for:", input_txt) 
        # st.write("You searched for:", input_txt) 
        # st.write(args, kwargs)
        


columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean',
    'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
    'fractal_dimension_se', 'radius_worst', 'texture_worst',
    'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst',
    'symmetry_worst', 'fractal_dimension_worst']


def getAllColumnData():
    array = []
    for lwe in all_lwes:
        array.append(lwe.getValue())
    a = np.array(array)
    return np.array([a])


def onSubmit():
    print("submit data with : ")
    array = getAllColumnData()
    print(array.shape)

    sc= load('std_scaler.bin')
    X_test_std = sc.transform(array)
    pred = model.predict(X_test_std)

    st.subheader(f"Result is {decode(pred[0])}")
    print("pred from input is " , pred[0])





# if __name__ == "__main__":
#     ...
st.button("Predict", key="predict button", on_click=onSubmit, type="primary")
all_lwes = []
for a in columns:
    lwe = LabelWithEditableField(a)
    all_lwes.append(lwe)

# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
    
    # getAllColumnData()

