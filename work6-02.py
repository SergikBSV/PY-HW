"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
 (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

from random import randint

minElementEnter = int(input("Введите минимальное значение элемента массива: "))
maxElementEnter = int(input("Введите максимальное значение элемента массива: "))
elementEnter = int(input("Введите число элементов массива: "))

startEnter = int(input("Введите начальное значение диапазона: "))
endEnter = int(input("Введите начальное значение диапазона: "))

def CreateArray(minElement, maxElement, element):
    array = [randint(minElement,maxElement) for el in range(element)]
    return array

def FindIndex(array, start, end):
    result = []
    for i in range(len(array)):
        if start < array[i] < end:
            result.append(i)
    return result

arrayOriginal = CreateArray(minElementEnter, maxElementEnter, elementEnter)
print("Оригинальный массив:")
print(arrayOriginal)
print(f'Индексы элементов массива, входящих в диапозон значений от {startEnter} до {endEnter}:')
print(FindIndex(arrayOriginal, startEnter, endEnter))