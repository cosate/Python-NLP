import nltk
wn = nltk.corpus.wordnet
ss = 0
nhypon = 0
for w in wn.all_synsets():
    ss+=1
    if len(w.hyponyms()) == 0:
        nhypon+=1
print(nhypon/ss)
