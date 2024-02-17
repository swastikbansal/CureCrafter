'''
import numpy as np
import json

from nltk_utilis import bag_of_words, tokenize, stem
with open('Text\Datasets\chatbot.json','r') as f:
    intents = json.load(f)
    
all_words = []
tags = 'symptoms'
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    if intent['tag'] = tags:
        for pattern in intent['patterns']:
            # tokenize each word in the sentence
            w = tokenize(pattern)
            # add to our words list
            all_words.extend(w)
            # add to xy pair
            xy.append(w)
        
# stem and lower each word and remove duplicates    
ignore_words = ['?', '!', '.','_']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
print(all_words)
'''
'''
import json
import nltk
from nltk.stem import PorterStemmer

# Load JSON file
with open('Text/Datasets/chatbot.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print("File loaded successfully")

# Initialize stemmer
stemmer = PorterStemmer()

# Iterate over intents
for intent in data['intents']:
    print(f"Processing intent with tag: {intent['tag']}")
    if intent['tag'] == 'symptoms':
        # Remove underscores and stem tokens
        stemmed_tokens = [stemmer.stem(pattern.replace('_', '')) for pattern in intent['patterns']]
        print(stemmed_tokens)
        '''
        
import json
import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# Load JSON file
with open('Text/Datasets/symptoms.json', 'r', encoding='utf-8') as f:
    intent = json.load(f)

# Iterate over intents
for intent in intent['intents']:
    #print("inside the intent loop.")
    if intent['tag'] == 'symptom':
        #print("inside the symptoms tag.")
        # Process each pattern
        for pattern in intent['patterns']:
            stemmed_tokens = [stemmer.stem(pattern.replace('_', ' ')) for pattern in intent['patterns']]
            print(stemmed_tokens)