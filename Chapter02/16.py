import nltk
br = nltk.corpus.brown

for cat in br.categories():
	l = len(br.words(categories=cat))
	s = len(set(br.words(categories=cat)))
	g = l/s
	words[cat]=l
	types[cat]=s
	grades[cat]=g
