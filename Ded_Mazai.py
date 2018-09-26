#! /usr/bin/python
import time
import os
import re



fromdate = input('Введите начало периода(Year-month-day): ') #Ввод даты начала периода
todate = input('Введите конец периода(Year-month-day): ') #Ввод даты конца периода


while True:
	try:
         fromdate = time.strptime(fromdate, "%Y-%m-%d")
         todate = time.strptime(todate, "%Y-%m-%d") #перевод к формату времени, проверка корректности введенных данных
	except ValueError:
		print ("Неверный формат даты")
	break

if (fromdate > todate): #Дата начала периода, не должна превышать дату конца периода
	print("Неверно указан период")
	quit()

saved = 0

for file in os.listdir('.'):  #берем файлы из текущей директории

	try:
		file_date = time.strptime(file, "%Y-%m-%d")   #перевод к формату времени
	except ValueError:
		continue

	if (file_date >= fromdate and file_date <= todate): #Попадает ли дата в указанный период

		for line in open(file):
			m = re.search("[0-9]+",line) #Поиск числового значения в файле
			if m is None:
				continue
			saved += int(m.group())


print ("Дед Мазай спас %d зайцев" % (saved))
















