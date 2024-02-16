import numpy 
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from nltk_utility import tokenize, stem, bag_of_words

from model import NeuralNet

with open('Datasets/intents.json', 'r') as f:
    intents = json.load(f)
    
all_words = []
tags = []
xy = []

for intent in intents[intents]:
    tag= intent['tag']
    
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))
        
ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train = []
y_train = []
for (patten_sentence,tag) in xy:
    bag = bag_of_words(patten_sentence, all_words)
    X_train.append(bag)
    
    label = tags.index(tag)
    y_train.append(label)
    
X_train = numpy.array(X_train)
y_train = numpy.array(y_train)

num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
output_size = len(tags)
print(input_size, output_size)

