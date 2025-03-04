#4. Есть список состоящий из 10 элементов типа int. Элементы задать с помощью библиотеки random. Список не упорядоченный.
#   Создать функцию_1, которая вернет отсортированный массив от меньшего к большему
#	 Создать функцию_2, которая вернуть отсортированный массив от большего к меньшему.
from random import randint
list = [randint(50, 150) for n in range(10)]   # Создал один исходный список
print('Исходный список: ',list)


# Сортировка по возрастанию

def bubble(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print('Сортировка по возрастанию: ', array)

bubble(list)


#  Сортировка по убыванию

def bubble_reverse(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print('Сортировка по убыванию: ',array )

bubble_reverse(list)
