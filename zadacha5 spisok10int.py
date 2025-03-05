#5.Есть список состоящий из 10 элементов типа int.
# Элементы задать с помощью библиотеки random. Список не упорядоченный.
# Элементы должны состоять из 3-х цифр (числа от 100 до 999).
# Написать функцию, которая выводит числа, у которых первая и третья цифры повторяются ( к примеру число 323, 121, 525, и т.п.).
# Если таких чисел в списке нет, вывести print об этом.
# Написать функцию, которая считает сумму цифр этого числа и выводит dict (к примеру число 555, сумма = 15.
# В dict будет 555: 15. И так 10 значений dict)
import random


def numbers(_list_):
    print(_list_)
    new_list = []
    for i in _list_:
        f = str(i)
        if (f[0] == f[2]):
            new_list.append(f)
    if not new_list:
        print('Подходящего числа(чисел) нет !')
    else:
        print('Числа подходящие условию: ',new_list)

_list_ = [random.randint(100, 999) for j in range(10)]
numbers(_list_)


def my_sum(_list_):
    my_dict = []
    for inte in _list_:
        summ =str(inte)
        math = int(summ[0]) + int(summ[1]) + int(summ[2])
        my_dict.append(math)
    print(my_dict)

_list_ = [random.randint(100, 999) for j in range(10)]
my_sum(_list_)
