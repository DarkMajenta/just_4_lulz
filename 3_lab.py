1. Conver
a = int(input("Курс: "))
i = 1
while i <= 20:
    print(i,"доллар = ",(i*a))
    i +=1
  
2. 
a = int(input("Число: "))
i = 1
while i <= 10:
    print("Произведение на ",i," = ",(i*a))
    i +=1


3. 

a = int(input("Первое число: "))
b = int(input("Второе число: "))
count = int(0)
i = int(0)
a1 = int(0)
if a <= b:
        while i != (b-a):
            a1 = (a*a)+a1
            i +=1
            a +=1
        print("Summ: ",a1);
else: print(" kekekekekekekekekeke ")


4. Не очень хорошая реализация, но работает.
a = (input("Число, скорее всего 5-значное"))
count = int(0)
b = a.split()
b = list(reversed(b))
while count != 5:
    b = a.split
    b = list(reversed(a))
    print("step result: ", b)
    count +=1
    print(count)
    
    
    
5.

a = int(input("N = "))
if 1 < a <= 10:
    print("OK. Working..") # чек числа на совместимость))
    cont_1 = int(1)
    cont_2 = int(0)
    i = int(0)
    while i < a :
        i+=1 # нужен ли такой счётчик или можно оптимизировать код
        cont_1 = i*cont_1 # тут происходит магия вычисления факториала для конкретного числа
        cont_2 +=cont_1 # тут происходит магия сложения факториалов
    print("Жобисдон") # чек работы цикла
print("Факториал ",a,"равен ",cont_1)
print("Их сумма ",cont_2)        

6.

count=int(0)
cont=float(input("Число последовательности "))
while cont < 0:
    cont = input("Число последовательности: ")
    count+=1
print("Шагов: ",count)

7. Что за изврат придумал данный синтаксис..


value = int(input("Значение n = "))
print("Первое число в последовательности возможно 1")
cont_1=int(0)
cont_2=int(1)
cont_3=int(0)
while cont_2 <= value:
      cont_3 = (cont_2+cont_1)
      cont_1 = cont_2
      cont_2=cont_3
print("Value = ",cont_2)


8. by Alina (aka pandazzz)

n = int(input("N = "))
a = int(0)
n1 = n
min_w = int(9)
k = 0
while n != 0:
    if (n%10) < min_w:
        a = n%10
        min_w = a
        k+=1
        print("result_step_to_min",k)
    n = n // 10;
k = 0;
print("N = ",n1, ' min = ',a)
while n1 != 0:
    if (n1%10) == min_w:
        k+=1
    n1 = n1 // 10
print("result_count: ",k)

9.

value = int(input("Число для проверки: "))
a = int(input("Первое число прогрессии: "))
if value > a:
    step = int(input("Шаг прогрессии: "))
    while value > a:
        a +=step
        print("Waiting..")
        if a == value:
            print("Данное число является частью прогрессии..возможно")
if value == a: print(" Realy??! ")
else: print("404 Bad maidcore O_o I'm bug! FIX ME!!1")


10-11


12. Скорее всего можно лучше оптимизировать код, пробуй и получится!

value = int(input("Факториал: "))
count = int(1)
ref = int(1)
if value == 1:
    print("Число = 1")
if value > 1:
    while value != ref:
        print("OK..working")
        count +=1
        ref = ref*count
        if value == ref:
            print("Число = ",count)
if value < 0:
    print("Отрицательный факториал?")
   
   
================================================
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
