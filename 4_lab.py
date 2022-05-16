1. Welcom to g0vnocode)))

from random import Random, random, randint
print("import_ok") #backtrace
n = int(20) #def_count_steps
a = [] # def_array
print(a,' empty array')
for i in range(n):
	def random_element():
		random_element=(random_element.random(163,190))
	#print(random_element,' insert this')
	a.append(random_element)
print(a)

2

a = []
b = int(input('1th: '))
step = int(input('Step: '))
for i in range(10):
	a.append(b+step)
	#print(a)
	#print('step cycle: ',i)
	b+=step
print(a)

3

s=input('Elements: ')#input with 'space'
a = s.split(' ')
print (a)
a.sort(reverse=True)
print(a)

4

a = []
b = []
for i in range (int(input('Колличество элементов: '))):
	a.append(int(input('Element: ')))
print(a)
for i in range (len(a)):
	#print('O____o')
	if i%2 == 0:
		#print(a[i])
		b.append(a[i])
	else:
		#print('-',a[i])
		b.append(-a[i])
print(b)

5
Непоняф задание

6

a = []
b = []
c = []
i=int(0)
print('For stop press !')
a.append(input('bug firsth elem 0__o'))
while a[i] != '!':
	i+=1
	a.append(input('Следующий: '))
	#print(a)
	if a[i] == '!':
		print(b)
		break
	if (int(a[i]))%2 == 0:
		b.append(a[i])
	if a[i].endswith('0'):
		c.append(a[i])	
print("i'll break")
print('Чётные: ',b)
print('Заканчиваются на ноль: ',c)


7

from random import randrange, randint
#from math import ldexp

print('Список имён абитуриентов')
math = []
russ = []
inf = []
name_list=[]
print('For stop press !')
name_list.append(input('press Enter'))
i=int(0)
while name_list[i] != '!':
	i+=1
	name_list.append(input('Следующий: '))
	#print(a)
	if name_list[i] == '!':
		name_list.pop(0)
		name_list.pop(-1)
		print(name_list)
		break
for i1 in range(i):
	s = (randint(0,100))
	i1+=1
	math.append(s)
	s = (randint(0,100))
	russ.append(s)
	s = (randint(0,100))
	inf.append(s)
	#math.append(Random.random(0,100))
result = []
i1 = 0
for i1 in range(i):
	
print(math,' ',russ,' ',inf )

16

n = int(input('N= '))
a=[]
for i in range(n):
	a.append(i*11)
	print(a)

===============================================================
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2021 vrl_mck

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
