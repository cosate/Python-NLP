import re

def load(f):
    file = open(f)
    s = file.read()
    file.close()
    return s

expression = '''
      \$?\d+(?:.\d+)*    #钱和百分号
    | \d{4,4}(?:-(?:(?:0[1-9])|(?:1[0-2])))(?:-(?:(?:[0-2][1-9])|(?:3[0,1])))#日期
    | [A-Z]\w+\s[A-Z]\w+  #人名
    '''

print(re.findall(expression,'Mike Pence 2016-11-17 $300.3',re.X))
