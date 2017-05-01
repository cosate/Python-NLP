import nltk

def bigramswithoutstopwords(text):
    bi = list(nltk.bigrams(text))
    biwithout = list()
    for b in bi:
        if not((b[0].lower() in nltk.corpus.stopwords.words('english')) or (b[1].lower() in nltk.corpus.stopwords.words('english'))):
            biwithout.append(b)
    freq = nltk.probability.FreqDist(biwithout)
    db = dict(freq)
    sd = sorted(db.items(),key=lambda b:b[1],reverse=True)
    print(sd[:50])
    return sd

bigramswithoutstopwords(nltk.corpus.reuters.words()[:100])
