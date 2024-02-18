
import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, word in enumerate(words):
        if word in tokenized_sentence:
            bag[idx] = 1
    return bag

# sentence='I am a worker and thank to have me here my head is paining with knee joints are also acking.'
# words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]

# bag = bag_of_words(tokenize(sentence), words)
# print(tokenize(sentence))
# print(bag)

