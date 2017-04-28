from nltk.book import *

def vocab_size(text):
    return len(set(text))

print(vocab_size(text1))
