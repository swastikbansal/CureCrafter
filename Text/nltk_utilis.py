
import numpy
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = numpy.zeros(len(words), dtype=numpy.float32)
    for idx, w in enumerate(words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag
'''
sentence='my head is paining with knee joints are also acking.'
print(tokenize(sentence))
for word in tokenize(sentence):
    print(stem(word))
'''
