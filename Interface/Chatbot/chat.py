import random
import json
import numpy as np
import pickle

import torch

from model import NeuralNet
from nltk_utilis import bag_of_words, tokenize


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open(
    "Interface\Chatbot\Datasets\intents.json", "r", encoding="utf-8"
) as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Predicting the symptome inputed
# with open('Interface\Chatbot\Datasets\symptomes.json', 'r') as json_data:
#     symptomes_file = json.load(json_data)

# symptomes = []
# for symptome in symptomes_file['intents']:
#     symptomes.append(symptome['tag'])
# # print(symptomes)

# #loading the Symptom Model
# symptom_model = torch.load('symptom.pth')

# symptom_model_state = symptom_model["model_state"]

# symp_model = NeuralNet(input_size, hidden_size, output_size).to(device)
# symp_model.load_state_dict(symptom_model_state)
# symp_model.eval()

bot_name = "CureCrafters"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    # token = tokenize(sentence)
    # for words in token:
    #     Y = bag_of_words(words, symptomes)
    #     Y = Y.reshape(1, Y.shape[0])
    #     Y = torch.from_numpy(Y).to(device)

    #     output = symp_model(Y)

    #     _, predicted = torch.max(output, dim=1)

    #     tag = tags[predicted.item()]
    #     print(tag)

    # for i in tokenize(sentence):
    #     pred = symp_model(i)

    sentence = tokenize(sentence)

    found_list = []

    # #Finding Symptoms in the sentence
    # for word in sentence:
    #     for w in word:
    #         if word in symptomes:
    #             found_list.append(word)
    #     else :
    #         for symptome in symptomes_file['intents']:
    #             if word in symptome['patterns']:
    #                 found_list.append(symptome['tag'])

    # print(found_list)
    # arr = np.zeros(len(symptomes))
    # for idx,word in enumerate(found_list):
    #     arr[symptomes.index(word)] = 1

    with open("finalized_model.sav", "rb") as file:
        diseas_model = pickle.load(file)

    # predicted_disease = diseas_model.predict([arr])

    # print(predicted_disease)

    # Making the prediction
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
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                # print(f"{bot_name}: {random.choice(intent['responses'])}")
                print(f"{bot_name}: ")

                for i in range(len(intent["responses"])):
                    print(intent["responses"][i])

                # Diseases and there symptoms
                with open("Interface\Chatbot\Datasets\disease_symptoms.csv", "r") as f:
                    print("Symptoms: ")
                    data = f.readlines()
                    # print(data)
                    for line in data:
                        # print(tag.lower(), line.split(',')[0].lower())
                        if tag.lower() in line.split(",")[0].lower():
                            for word in line.split(",")[1:]:
                                if word != "":
                                    print(word)
                            break

    else:
        print(f"{bot_name}: I do not understand...")
