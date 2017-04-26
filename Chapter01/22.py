from nltk.book import *
vof4 = [w for w in text5 if len(w) == 4]
print(len(vof4))
print(vof4[:50])
freq = FreqDist(vof4)
a = sorted(freq)
print(type(a))
print(len(a))
print(a[:50])
for w in a.keys() and i in range(50):
    print(w)
    print(a[w])
