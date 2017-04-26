sent3 = ['In','the','beginning','God','created','the','heaven','and','the','earth','.']
print(sent3.index('the'))
print('\n')
for i in range(len(sent3)):
    if sent3[i] == 'the' and i != sent3.index('the'):
        print(i)
