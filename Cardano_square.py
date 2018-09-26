# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:01:24 2017

@author: Evgenii
"""

def str_to_list(string):
    for i in range(len(string)):
        coding_string.append(string[i])
    return coding_string
        
# Функция кодирования строки, с помощью квадрата Кардано
def coder(cardano,string):
    count=0

    for s in range(4): # 4 цикла, т.к. делаем поворот на 90 градусов 4 раза
        for i in range(len(cardano)): # Проходим по массиву, когда попадаем в окошко, вписываем первый символ строки, 
            for j in range(len(cardano[i])): # в закодированную страницу
                               if cardano[i][j]==1:
                                   coded_text[i][j] = coding_string[count]
                                   count += 1 #переход к следующему элементу кодируемой строки 
        cardano = tuple(zip(*cardano[::-1])) # Поворот квадрата на 90 градусов 

    return ("".join("".join(x) for x in coded_text)) # преобразуем двумерный список к строковому представлению
    
# Функция декодирования строки, с помощью квадрата Кардано   
def decoder(cardano,text):
    Decrypted = ""
    for s in range(4):# 4 цикла, т.к. делаем поворот на 90 градусов 4 раза
        for i in range(len(cardano)): # Когда попадаем в окошко, записываем символ 
            for j in range(len(cardano[i])): # в раскодированную строку
                               if (cardano[i][j]==1):
                                   Decrypted += text[i][j]
        cardano = tuple(zip(*cardano[::-1])) # Поворот квадрата на 90 градусов 
    
    
    return Decrypted     


if "__main__" == __name__:
    
    cardano4 = [[0,0,1,0],
               [0,0,0,1],
               [0,1,0,0],
               [1,0,0,0]]
    text4 = [['з','т','п',' '],
            ['о','ж','ш','р'],
            ['е','и','г','а'],
            ['е','с','ю','о']]
    cardano5 = [[0,1,0,1,0],
               [0,0,0,0,0],
               [0,0,0,1,0],
               [0,1,0,0,0],
               [1,0,1,0,0]]
    text5 = [['з','т','п',' ',' '],
            ['о','ж','ш','р',' '],
            ['е','и','г','а',' '],
            ['е','и','г','а',' '],
            ['е','с','ю','о',' ']]
            
    coded_text = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

    string4 = 'приезжаю шестого'
    string5 = 'приезжаю шестого или нет'
    coding_string=[]
    str_to_list(string5)
    print("Строка, которую необходимо зашифровать: ", string5)
    print("Закодированная строка - ",coder(cardano5,string5))
    print("Раскодированная строка - ",decoder(cardano5,coded_text))














