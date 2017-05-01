import nltk

def word_freq(word,text):
    te=nltk.corpus.brown.words(categories=text)
    freq=nltk.probability.FreqDist(te)
    return freq[word]/len(te)

print(word_freq('the','fiction'))
