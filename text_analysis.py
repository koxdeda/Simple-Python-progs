#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import csv

try:
	f = open("Vistrel.txt","r")
except:
	print('Error!')
f = f.decode('utf8')
text = f.read()
#print(text)
f.close()

dct= {}
mas=[]
text = text.replace('?','.').replace('!','.').replace(' - ',' ')
sentences = text.split('.')

for i in sentences:
    print(len(i.split(' ')))
    print(i)
    count_word=len(i.split(' '))
    mas.append(count_word)

def analysis():
    for i in mas:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

analysis()
for i in sorted(dct):
   print("Из %d слов  - %d предложений" %  (i,dct[i]))
print(dct)
f = f.encode('utf8')
with open('graphictest.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['words','sentences'], extrasaction='ignore', delimiter = ';')
    writer.writeheader()
    for key, value in dct.items():
        writer.writerow({'words': key, 'sentences': value})








