import nltk
cmu = nltk.corpus.cmudict.entries()

freq = nltk.FreqDist([w[0] for w in cmu])
a=0
for key in freq.keys():
    if freq[key] != 1:
        a+=1
print(a/len(cmu))
