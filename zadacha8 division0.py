#8. Напиши функцию, которая принимает число и внутри делит его на 0.
# Используй Try Except. При Except ptint(что-то).
def _try(number):
    try:

        answer = number/0
        print(answer)
    except:
        print('Вычисление прошло неудачно!')
    print('Завершение программы')

number = int(input('Введите число:'))
_try(number)