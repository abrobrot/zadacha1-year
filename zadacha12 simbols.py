#12. Напиши функцию, которая удаляет первые n символов из строки, и вернет новую строку.
def _remake(old_string):
        numbers = int(input('Введите количество символов: '))
        old_string = old_string[numbers:]
        print(old_string)

old_string = str(input('Введите строку: '))
_remake(old_string)
