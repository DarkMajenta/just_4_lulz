За сырцы стоит поблагодарить многих людей из интернетов!


1. Области абсцисс

print("Kono Dio Da!") #стоит ли реализовывать тут циклы?
print("Значение по оси абсцисс: ")
x = int(input())
if x>4:
    print("Это область II")
if x<4:
    print("Это область I")
else:

    print("Точка попала на границу деления областей")

2. Области ординат

print("Kono Dio Da!") #стоит ли реализовывать тут циклы?
print("Значение по оси ординат: ")
x = int(input())
if x>3:
    print("Это область II")
if x<3:
    print("Это область I")
else:
    print("Точка попала на границу деления областей")

3. Простое условие

print("Kono Dio Da!") #стоит ли реализовывать тут циклы?
print("Значение по оси абсцисс: ")
x = int(input())
print("Значение по оси ординат: ")
y= int(input())
if x == y and (x<2) and (y <= 2):
    print("Первая функция")
if x == (y*(-1)) and (y <= -3):
    print("Вторая функция")
if y == 2 and x >= 2 :
    print("Первая функция")
if y == -3 and x >= 3 :
    print("Вторая функция")
else: print("Out of range")

4.

a = int(input("Первое число: "))
if int(input("Второе число: ")) < a:
    print ("Первое больше")
else: print("Второе больше")
/// забыл реализацию равнозначных чисел

5.

a = int(input("Первое число: "))
a1 = int(input("Второе число: "))
if a > a1:
    print("Max: 1th, Min: 2th")
elif a < a1:
    print("Max: 2th, Min: 1th")
elif a == a1:
    print("equal")
  
  
6.

a = int(input("Год рождения:"  ))
a1 = int(input("Месяц рождения: "))
b = int(input("Сегодняшний год:" )) - a
if (int(input("Сегодняшний месяц: ")) > a1):
    b = b+1
    print("Age: ", b)
else: 
    b = b-1
    print("Age: ", b)

7. 

import math
print("Только целые числа")
x = int(input("Значение x: "))
if x > 0 :
    x = sin(sqr(x))
    print("Значение y:", x)
elif x < 0:
    x = 1 - 2*(sqr(sin(x)))
    print("Значение y:", x)
  
  
8. 

import math
print("Только целые числа")
x = int(input("Значение x: "))
if x > 0 :
    x = sin(sqr(x))
    print("Значение y:", x)
elif x < 0:
    x = 1 + 2*((sqr(sin(x))))
    print("Значение y:", x)
  
  
9. 

import math
a = float(input('Первое число: '))
b = float(input("Второе число: "))
if a < b:
    a = abs(a-b)
    b = abs(a-b)
    print("a = ",a," b = ",b)
if a > b:
    b = abs(a-b)
    a = abs(a-b)
    print("a = ",a," b = ",b)
    
    
10. 

n = int(input())
if n % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')
 
if n % 10 == 7:
    print('Число оканчивается на 7')
else:
    print('Число не оканчивается на 7')


11.

import math
a = int(input('Первое число: '))
b = int(input("Второе число: "))
if a > b:
    print("Первое больше второго")
else:
    print("Второе больше первого")
if (a//10 == b//10):
    print("Первые числа одинаковы")
if (a%10 == b%10):
    print("Вторые числа одинаковы")
if (a%10 == b%10) and (b//10 == a//10):
    print("Error 404")
else: print("IDK")


12.

import math
a = int(input('Трёхзначное число: '))
if a%10 == a//100:
    print("Является")
else: print("Bad Gatway 502")

13.

import math
a = int(input('Трёхзначное число: '))
if a%10 == a//100 == (a//10)//10:
    print("a)Что-то там..")
else: print("a)Не что-то там..")
if a%10 == a//100 or a%10 == (a//10)//10 or a//100 == (a//10)//10:
    print("b)Что-то там..")
else: print("b)Не что-то там..")


14.

import math
a = int(input('4исло: '))
if a%2 == 0:
    print("Чётное число")
else: print("Не чётное число")


15.

import math
a = int(input("Минуты: "))
if ( 0 <= a%10 <= 3) or ( 5 <= a%10 <=8):
    print("Green signal")
else: print("Red signal")

16.

import math #флуд пашет через точку
a = float(input('Масса: '))
print("Без учёта гравитации: ",math.ceil(a))

17.

import math
a = ((543*130)//(130*130))
print("Ohh crap..", a)


18.



19.

import math
a = int(input("Трехзначное число: "))
print("Прочтение наоборот: ", (a%10),(a//10)%10,(a//100))


20.
import math#?????
a = int(input("Трехзначное число: "))
print("Прочтение наоборот: ", (a//10)%10,(a%10),((a//100)))

21

22

23

24. 
a = int(input("Трёхзначное число: "))
i = 1 #lol
if ((a//10)%10) != (a%10) != ((a//100)):
    print(" OK ")
    while i <= 6:
     b = int(((a%10)*100)+((a//100)*10)+((a//10)%10))
     a = b
     print("Example: ",b)
else: ("Ohh crap")

25.

import math
a = int(input("число: "))
if a > 9:
    print("Единиц: ", a%10," Десятков: ", a//10)
else: print("Число меньше 9 и единиц в нём: ", a)

==========================================================================================================================
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

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
