#11. Напиши рекурсивную функцию для вычисления факториала числа.
def factorial(numb):
    if (numb <= 1):
        return 1
    else:
         return (numb * factorial(numb - 1))

numb = int(input('Введите число: '))
print('Факториал равен:',factorial(numb))
