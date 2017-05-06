import re
import urllib.request
import nltk

def unknown(url):
    html = urllib.request.urlopen(url)
    content = html.read().decode()
    l = re.findall('[a-z]+',content)
    res = list()
    for w in l:
        if w not in nltk.corpus.words.raw().split():
            res.append(w)
    return res

print(unknown('http://www.zhihu.com'))
