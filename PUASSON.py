#! /usr/bin/python
# -*- coding: utf 8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import random as rnd
import stat


def analysis(mas):
    for i in mas:
        if i in rez:
            rez[i] += 1
        else:
            rez[i] = 1





m = 2**16 - 1; #параметр распределения (хз что)
k = 35413.58249; #параметр распределения (хз что)
T = 65000; #длина массивов
#T=1000
a=0.003 #мат ожидание для пуассона
PSL = np.zeros((T,1)) #подготовительная последовательноссть
Mat_WPSL = np.zeros((T,1)) #мат ожидание ДО
Mat_WPSN = np.zeros((T,1))
RND_POSL = np.zeros((T,1)) #случайная последовательность
PSN_REZ=np.zeros((T,1)) #результат работы пуассона
EXPON=np.zeros((T,1)) #после работы экспоненты
WHOLE=np.zeros((T,1)) #целочисленный массив
PSL = np.zeros((T,1)) #подготовительная последовательноссть

RND_POSL = np.zeros((T,1)) #случайная последовательность
#PSN_POSL=np.zeros((T,1)) #результат работы пуассона

PSN_POSL=[]
PSN_RASPR=[]
PSL[0]=1
WHOLE[0]=0
EXPON[0]=0
RND_POSL[0]=0
PSN_POSL=[]
Disp_upb = 0
Disp_upa = 0

rez={}
Mo=0.0
lmbd=0.133
count=0


#RND_POSL=np.random.randint(25, size=(T))

RND_POSL[0] = PSL[0]/m;         #создание собственной случайной последовательности

for i in range(1,T):
   PSL[i] = ((k*PSL[i-1])%m);
   RND_POSL[i] = (PSL[i]/m);

#print (RND_POSL)

nchunks = 100
chunks = [RND_POSL[x:x+nchunks] for x in range(0, len(RND_POSL), nchunks)]
#print (chunks)
for i in range (0,len(chunks)):
    for j in range(0,nchunks):
        if(chunks[i][j])>lmbd:
            count+=1
    #print(count)
    PSN_POSL.append(count)
    count=0
#print(PSN_POSL)
#print(len(PSN_POSL))

analysis(PSN_POSL)
print(rez)


Mo=sum(PSN_POSL)/len(PSN_POSL)
D_up = 0.0

for i in range(0,len(PSN_POSL)):
    D_up = D_up + (Mo - PSN_POSL[i])**2;
D = D_up/len(PSN_POSL);

Mo=Mo/100
D=D/100
#Dis=stat.dispersion(PSN_POSL)
print(u'Matematicheskoe ozhidanie=', Mo)
print(u'Dispersia=', D)
for key,value in rez.items():
    plt.bar(key,value)
    plt.xlabel(u'Число превышений')
    plt.ylabel(u'Значение количества превышений')
    plt.ylim(0,99)
plt.show()


#plt.hist(RND_POSL,50, color='r')
#plt.show()
#plt.hist(EXPON,50, color="pink")
#plt.show()
#plt.hist(PSN_REZ,50, color="cyan");
#plt.hist(WHOLE, 50, color="green")
#plt.show()