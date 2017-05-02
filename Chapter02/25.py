import nltk

lang = list()
def find_language(string):
    for file in nltk.corpus.udhr.fileids():
        if file.endswith('Latin1'):
            if string in nltk.corpus.udhr.words(file):
                lang.append(file)
    return lang

print(find_language('the'))
