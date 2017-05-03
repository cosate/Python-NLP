import re
import urllib.request

html = urllib.request.urlopen('http://www.nltk.org/')
content = html.read().decode()

rd = re.compile('<[\s\S]*?>')
print(rd.sub('',content))
