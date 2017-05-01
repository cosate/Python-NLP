import nltk
import nltk.probability as pro
br = nltk.corpus.brown

cfd = pro.ConditionalFreqDist([(genre,word) for genre in br.categories()
                               for word in ['can','could','may','might']
                               for w in br.words(categories=genre)
                               if word == w])
cfd.tabulate()
