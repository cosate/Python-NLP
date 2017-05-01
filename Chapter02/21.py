import nltk
from nltk.book import *
def voice(text):
    en = nltk.corpus.cmudict.entries()
    dic = dict()
    for i in range(len(en)):
        dic.update({en[i][0]:i})
    vo=0
    for w in text:
        if w in dic.keys():
            vo+=len(en[dic[w]][1])
    print(vo)
    return vo

voice(text1)
        
