from nltk.book import *
def percent(word,text):
    a = 0
    for w in text:
        if w == word:
            a+=1
    return a/len(text)

print(percent('help',text5))
