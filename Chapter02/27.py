import nltk
wn = nltk.corpus.wordnet

allsynsn = wn.all_synsets('n')
n = list()
for syn in allsynsn:
    n += syn.lemma_names()

nd = set(n)
sumofn = 0
for i in nd:
    sumofn += len(wn.synsets(i,'n'))

print('n',sumofn/len(nd))

allsynsv = wn.all_synsets('v')
v = list()
for syn in allsynsv:
    v += syn.lemma_names()

vd = set(v)
sumofv = 0
for i in vd:
    sumofv += len(wn.synsets(i,'v'))

print('v',sumofn/len(vd))

allsynsadj = wn.all_synsets('a')
adj = list()
for syn in allsynsadj:
    adj += syn.lemma_names()

adjd = set(adj)
sumofadj = 0
for i in adjd:
    sumofadj += len(wn.synsets(i,'a'))

print('a',sumofn/len(adjd))

allsynsadv = wn.all_synsets('r')
adv = list()
for syn in allsynsadv:
    adv += syn.lemma_names()

advd = set(adv)
sumofadv = 0
for i in advd:
    sumofadv += len(wn.synsets(i,'r'))

print('r',sumofn/len(advd))
