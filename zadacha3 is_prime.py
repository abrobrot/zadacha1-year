#написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое,и False - иначе.
def is_prime(number):
    if number == 1:
         return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

number=int(input('Введите число: '))
print('Ответ: ',is_prime(number))

