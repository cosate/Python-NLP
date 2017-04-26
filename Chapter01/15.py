from nltk.book import *
res=[]
for w in set(text5):
    if w.startswith('b'):
        res.append(w)

print(sorted(res))

