1. Try using only one a

print("Значение a: ")
a=int(input())
print("Значение b: ")
a=int(input())+a
print("result a+b = " )
#print(b)
print(a)

2. Triangle area
//Опираясь на формуле из задания, а именно s=0,5*(b*h)

print('Value of b: ')
b = float(input())
print('Value of h: ')
b = ((float(input())*b)*0.5) #Может быть избыточныам решением, но как пример подойдёт
print("Area: ")
print(b)

3. Orange Box. В данной задаче вынуждены использовать 3 переменных, по скольку 2 используются для хранения данных, но питон позволяет решить и эту проблему..

print("Колличество детей: ")
count = int(input())
print ("Коллчество пиписинов: ")
count_2 = int(input())
div = (count_2/count)
print("Проверка деления: ")
print(div)
div = (count_2/count)
print("Check // : ")
print(div)
print("Check % : ")
div = (count_2%count)
print(div)

4. Clock

print("Колличество минут: ")
a = int(input())
b = a % (60 * 24) // 60
a = a % 60
print("check: ")
print(b, a)

5. HellO_world

print("It's me! Dio!!")
print("Please, input you addiction word: ")
a = input() #могут возникнуть проблемы с нехваткой памяти из-за переменной
print("Hello, "+a+"!")

6. Count

print("It's me! Dio!!")
print("Задаём число: ")
a = ((int(input()))+1)
print("Следующее число:" )
print(a)
a = a-2
print("Предыдущее число: ")
print(a)

7. Шнурки. Well..

print("Значение a: ") #можно использовать
a = int(input())
print("Значение b: ") #может использоваться
b = int(input())
print("Значение l: ") #придётся хранить отдельно
l = int(input())
print("Значение N: ") #так же пока что будет отдельно висеть
count = int(input())
a = ((((a+b)*2)*(count-1))+((l*2)+a))
print("Предполагаемая длина шнурка:")
print(a)
================================================
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2021  pandazzz, vrl_mck 

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
