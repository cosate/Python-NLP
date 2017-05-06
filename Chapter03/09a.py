import re

def load(f):
    file = open(f)
    s = file.read()
    file.close()
    return s

expression = '''
    (?:[A-Z]\.)+            #缩写
    | \w+(?:-\w)*         #单词
    | \$?\d+(?:.\d+)?%?   #钱和百分号
    | \.\.\.            #省略符
    | [][.,;"'?():-_‘]  #标点符号
    '''

print(re.findall(expression,load('text-test09.txt'),re.X))
