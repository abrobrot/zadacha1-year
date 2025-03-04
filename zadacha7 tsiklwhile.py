#7. Напиши функцию с циклом While, которая принимает на вход число, и делит его на 5 (к примеру) и потом отнимает -1.
# Дели это число до тех пор, пока. Когда число станет меньше 0, выведи количество итераций, сделанных в этой функции.
def division(number):
    iteration=0
    while number > 0 :
        number = (number / 2) - 1
        iteration=iteration+1
    return iteration
number=int(input('Введите число: '))
print('Количество итераций: ',division(number))