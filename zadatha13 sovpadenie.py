#13. Напиши функцию, которая возвращает True, если первый и последний номер в списке совпадает.
# В случае, если не совпадает, верните значение False. Список задается рандомно.
# Какие элементы внутри - ты не знаешь.
from random import randint
my_list = [randint(1, 5) for n in range(10)]


def mismatch(my_list):
    if my_list[0] == my_list[-1]:
        return True
    else:
        return False

print('Совпадают ли первый элемент с последним: ',mismatch(my_list))
