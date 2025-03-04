#6. Есть список состоящий из 1000 элементов типа int. Элементы задать с помощью библиотеки random.
# Создать функцию,которая принимает список и выводит количество четных и не четных элементов.
# Вывести в формате dict ("кол во четных": 10, "кол во нечетных" : 990)
import random
list = [random.randint(1, 1000) for j in range(1000)]
def dictionary(list):
    dict={}
    even_number=0
    non_even_number=0
    for i in list:
        if i % 2 == 0:
            even_number=even_number+1
        else:
            non_even_number=non_even_number+1
    dict['Четных элементов'] = even_number
    dict['Нечетных элементов'] = non_even_number
    return dict
print(dictionary(list))
