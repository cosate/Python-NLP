import nltk
wn = nltk.corpus.wordnet

allsyn = wn.all_synsets('n')
als = list(allsyn)
allsyn = wn.all_synsets('n')

sumofhypon = 0

for syn in allsyn:
    sumofhypon += len(syn.hyponyms())


print(len(als))
print(sumofhypon)
print(sumofhypon/len(als))
