from nltk.corpus import swadesh
de2en = swadesh.entries(['de','en'])
it2en = swadesh.entries(['it','en'])

translate = dict(de2en)
translate.update(it2en)

#可能存在德语和意大利语同词不同意的现象；将字典值作为一个list，存储两个对应英语词，如果存在的话
