import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import torch


raw_df = pd.read_csv("Text/Datasets/Sym-DiseaseTraining.csv")
raw_df.info()

input_data = raw_df.iloc[:,:-1]
output_data = raw_df.iloc[:,-1]

print(input_data)

itrain,ivar, otrain, ovar = train_test_split(input_data, output_data, test_size=0.1,random_state=30)

print(itrain.shape)
print(otrain.shape)
print(ivar.shape)
print(ovar.shape)

Text_model = RandomForestClassifier(n_jobs=-1, random_state=30)
Text_model.fit(itrain,otrain)

Text_model.score(itrain,otrain)

test_data = pd.read_csv("Text/Datasets/Sym-DiseaseTesting.csv")
test_input= test_data.iloc[:,:-1]
test_output= test_data.iloc[:,-1]
output = Text_model.predict(test_input)
print(output)

Text_model.score(test_input,test_output)

import pickle
filename = 'finalized_model.sav'
pickle.dump(Text_model, open(filename, 'wb'))

def prediction(data):
    parameter = np.array(data).reshape(1, -1)
    reopen_file = 'finalized_model.sav'
    loaded_model = torch.load(reopen_file)
    loaded_model.eval()
    parameter_tensor = torch.tensor(parameter, dtype=torch.float).to('cpu')
    predict = loaded_model(parameter_tensor)
    _, predicted = torch.max(predict.data, 1)
    return predicted.item()
