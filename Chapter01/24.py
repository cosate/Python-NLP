from nltk.book import *
a=[]
b=[]
c=[]
d=[]
for w in text6:
    if w.endswith('ize'):
        a.append(w)
    if 'z' in w:
        b.append(w)
    if 'pt' in w:
        c.append(w)
    if w.istitle():
        d.append(w)
        
print(a)
print(b)
print(c)
print(d)
