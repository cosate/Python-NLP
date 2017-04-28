import nltk
cfd = nltk.ConditionalFreqDist([(con,year[:4]) for year in nltk.corpus.state_union.fileids() for word in nltk.corpus.state_union.words(year) for con in ['men','women','people'] if word == con])
cfd.plot()
