import nltk
wn = nltk.corpus.wordnet

fi = ['car','gem','journey','boy','coast','asylum','magician','midday',
      'furnace','food','bird','bird','tool','brother','lad','crane','journey',
      'monk','cemetery','food','coast','forest','shore','monk','coast','lad',
      'chord','glass','rooster','noon']
se = ['automobile','jewel','voyage','lad','shore','madhouse','wizard','noon',
      'stove','fruit','cock','crane','implement','monk','brother','implement',
      'car','oracle','woodland','rooster','hill','graveyard','woodland',
      'slave','forest','wizard','smile','magician','voyage','string']

similarity = list()
for i in range(len(fi)):
    first = fi[i]
    second = se[i]
    sim = 0.0
    for syn1 in wn.synsets(first):
        for syn2 in wn.synsets(second):
            si = syn1.path_similarity(syn2)
            if si != None:
                if si > sim:
                    sim = si
    similarity.append(sim)

print(len(fi))
print(len(se))
print(len(similarity))
print(similarity)
