import re

file = open('text-test19.txt')

cont = file.readlines()

for i in range(len(cont)):
    cont[i] = re.sub(r'\n','',cont[i])

res = []
for w in cont:
    res.append([w.split()[0],int(w.split()[1])])

print(res)
