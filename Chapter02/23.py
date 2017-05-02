import nltk
import pylab
import random
def zif(text):
    freq = nltk.probability.FreqDist(text)
    freq = dict(freq)
    f = sorted(freq.items(),key=lambda x:x[1],reverse=True)
    pylab.plot(range(1,len(f)+1),[k[1] for k in f])
    pylab.show()

def rand():
    s = ''
    for i in range(100):
        s+=random.choice('abcdefg ')
    return s

s=''
for i in range(100):
    s+=' '
    s+=rand()

s=s.split()

zif(s)
