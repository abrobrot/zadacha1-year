#14. Напиши функцию, которая на вход получает два списка.
# Из первого списка, извлекаются нечетные числа, из второго четные.
# Новые элементы добавляем в новый список. Возвращай список.
def _combining(end_list):
    first_list= input('Введите первый список: ')
    wordes_first = first_list.split(' ')
    second_list = input('Введите второй список: ')
    wordes_second = second_list.split(' ')
    for numbers_first in wordes_first:
       if int(numbers_first) % 2 == 0:
            end_list.append(numbers_first)
    for numbers_second in wordes_second:
        if int(numbers_second) % 2 != 0:
            end_list.append(numbers_second)
    print('Список обработанный функцией: ', end_list)

end_list = []
_combining(end_list)