import random
import json

import torch

from model import NeuralNet
from nltk_utilis import bag_of_words, tokenize

import numpy as np

import pickle


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('Text\Datasets\intents.json', 'r',encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#Predicting the symptome inputed
with open('Text\Datasets\symptomes.json', 'r') as json_data:
    symptomes_file = json.load(json_data)

symptomes = []
for symptome in symptomes_file['intents']:
    symptomes.append(symptome['tags'])
print(symptomes)

bot_name = "Sam"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break
    
    sentence = tokenize(sentence)
    
    found_list = []
    
    for word in sentence:
        if word in symptomes:
            found_list.append(word)
        else :
            for symptome in symptomes_file['intents']:
                if word in symptome['patterns']:
                    found_list.append(symptome['tags'])
                    
    # for idx,word in enumerate(found_list):
    #     if " " in word:
    #         print(word)
    #         word = word.replace(" ", "_")
    
    # print(symptomes)
    # print(found_list)
    
    arr = np.zeros(len(symptomes))        
    for idx,word in enumerate(found_list):
        arr[symptomes.index(word)] = 1     
    
    with open('finalized_model.sav', 'rb') as file:
        diseas_model = pickle.load(file)
    
    predicted_disease = diseas_model.predict([arr])
    
    print(predicted_disease)
    
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    # print(tag)
    
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                # print(f"{bot_name}: {random.choice(intent['responses'])}")
                print(f"{bot_name}: ")
                
                for i in range(len(intent['responses'])):
                    print(intent['responses'][i])
                
                with open('Text\Datasets\disease_symptoms.csv', 'r') as f:
                    print("Symptoms: ")
                    data = f.readlines()
                    # print(data)
                    for line in data:
                        # print(tag.lower(), line.split(',')[0].lower())
                        if tag.lower() in line.split(',')[0].lower():
                            for word in line.split(',')[1:]:
                                if word != '':
                                    print(word)   
                            break
                                        
    else:
        print(f"{bot_name}: I do not understand...")
