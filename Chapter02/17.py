import nltk
from nltk.corpus import stopwords
def usewords(text):
	stopwords=nltk.corpus.stopwords.words('english')
	use = [w for w in text if w.lower() not in stopwords]
	freq = nltk.probability.FreqDist(use)
	du = dict(freq)
	su = sorted(du.items(),key=lambda d:d[1],reverse=True)
	print(su[:50])
	return use

usewords(nltk.corpus.reuters.words())
