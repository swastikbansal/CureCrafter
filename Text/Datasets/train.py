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

