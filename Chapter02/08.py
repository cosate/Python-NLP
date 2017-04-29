import nltk
names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist([(con,chr(alp)) for alp in range(65,91) for con in names.fileids() for w in names.words(con) if w.startswith(chr(alp))])
cfd.plot()
