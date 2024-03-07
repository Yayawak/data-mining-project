import pickle
import pandas as pd

def loadModel():
    filename='./finalized_model.sav'
    model = pickle.load(open(filename, 'rb'))
    return model

# data = pd.read_csv("/content/sampledata.csv")
# X_test = data
# y_pred=model.predict(X_test)
# y_pred