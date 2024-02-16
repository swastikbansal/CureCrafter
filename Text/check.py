import numpy as np
import json

from nltk_utilis import bag_of_words, tokenize, stem
with open('Text\Datasets\chatbot.json','r') as f:
    intents = json.load(f)
    
all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to xy pair
        xy.append((w, tag))
        
# stem and lower each word and remove duplicates    
ignore_words = ['?', '!', '.']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
print(all_words)

