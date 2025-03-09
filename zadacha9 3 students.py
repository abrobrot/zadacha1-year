# 9. Создай словарь с информацией о трех студентах (имя, возраст, курс). Выведи информацию о каждом студенте.
def students_dict(students):
    number_of_students = int(input('Введите количество студентов: '))
    for numb in range(number_of_students):
        dictofstudents = {}
        dictofstudents.update({'Имя': input('Введите имя: '),
                               'Возраст': input('Введите возраст: '),
                               'Курс': input('Введите курс: ')})
        students.append(dictofstudents)
    for numb in range(number_of_students):
        print(students[numb])

students = []
students_dict(students)
