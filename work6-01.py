"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

startEnter = int(input("Введите первый элемент массива: "))
stepEnter = int(input("Введите шаг прогрессии: "))
quantityEnter = int(input("Введите число элементов массива: "))

def CreateArray(start, step, quantity):
    array = []
    array.append(start)
    n = 1
    while n < quantity:
        start += step
        array.append(start)
        n += 1
    return array

print("Финальный массив:")    
print(CreateArray(startEnter, stepEnter, quantityEnter))

