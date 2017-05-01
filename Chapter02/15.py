import nltk
import nltk.probability as pro

br = nltk.corpus.brown
freq = pro.FreqDist([ w for cat in br.categories() for w in br.words(categories=cat)])

word3 = [w for w in freq.keys() if freq[w]>3]
print('长度大于3的词共有',len(word3),'个')
