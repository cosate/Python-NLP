import nltk
per = nltk.corpus.gutenberg.words('austen-persuasion.txt')
print(len(per))
print(len(set(per)))
