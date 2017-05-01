import nltk
wn = nltk.corpus.wordnet

def supergloss(s):
	st=s.definition()
	for ho in s.hyponyms():
		st+='; '
		st+=ho.definition()
	for he in s.hypernyms():
		st+='; '
		st+=he.definition()
	return st
