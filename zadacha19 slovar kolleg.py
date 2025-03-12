#Дан словарь коллег ( формат смотри на скрине ). Ключ - фамилия. Значение - зп (int или float тип)
#Вывести
#1. Среднюю зп коллектива
#2. Фамилию сотрудника с самой высокой и с самой низкой зп
#3. Разницу в процентах между самый низкой и самой высокой зп
#4. Количество сотрудников фамилия которых начинается с буквы I
#5. Количество сотрудников женского поля
#6. Количество сотрудников мужского пола
# Также сделать функцию, которая создаст новый словарь, состоящий из перых трех и последних трех сотрудников.
# В конце нового словаря добавить ТВОЮ фамилию и твою зп.


people={
    'Ivanov': 60234,
    'Smirnov': 74459,
    'Sobolev': 69333,
    'Vasilev': 34596,
    'Stepanov': 49568,
    'Andreeva': 55678,
    'Vasileva': 47834,
    'Mishkova': 66800}


zp = 0
quantity = 0
for salary in people.values():
    zp += salary
    quantity += 1
average = zp/quantity
print('Средняя зарплата в коллектива:',average)


max_salary = 0
for numbers in people.values():
    if numbers > max_salary:
        max_salary = numbers
print('Самая большая зп:', max_salary)


min_salary = max_salary
for numbers in people.values():
    if numbers < min_salary:
        min_salary = numbers
print('Самая маленькая зп:', min_salary)

difference = (max_salary / min_salary) * 100
print('Разница между самой большой и самой меньшей зп:', int(difference), '%')

women = 0
men = 0
surname = people.keys()
for numb in people:
    if 'a' == numb[-1]:
        women += 1
    else:
        men += 1
print('Количество женщин в коллективе:', women)
print('Количество мужчин в коллективе:', men )


def my_colleagues(people):
    new_people={}
    new_ = 0
    _new = 0
    for one in people.items():
        new_ += 1
        if new_ < 4:
            new_people.update([one])
    for one in reversed(people.items()):
        _new += 1
        if _new < 4:
            new_people.update([one])
    new_people['Stakhov'] = 123453

    print(new_people)

my_colleagues(people)


