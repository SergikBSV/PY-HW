"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""


n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

arr_n = list()
for i in range(n):
    el = int(input(f'Введите {i + 1} элемент первого набора: '))
    arr_n.append(el)

arr_m = list()
for i in range(m):
    el = int(input(f'Введите {i + 1} элемент второго набора: '))
    arr_m.append(el)

arr_fin = sorted(set(arr_n).intersection(set(arr_m)))
print(*arr_fin)