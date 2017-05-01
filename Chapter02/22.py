def hedge(text):
    b = range(0,len(text)+1,3)
    c = list(b)
    c.reverse()
    c.pop()
    for i in c:
        text.insert(i,'like')
    return text

a = hedge(['de','fr','yt','fr','ew','fv','as','yu','4t5','7ju','78yt','tr5','t'])

print(a)
