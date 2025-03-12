#16. Напиши функцию, которая определяет, входит ли слово в строку, или нет.
# Если не входит, то добавь это слово в конце строки.
def _find(_string):
    _string = input('Ведите строку: ')
    my_word = input('Введите слово: ')
    if my_word in _string:
        print('Слово присутствует в строке!')
    else:
        _string += ' ' + my_word
        print('Строка с добавленным словом: ',_string)

_string = []
_find(_string)
