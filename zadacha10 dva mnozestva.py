#10. Создай два множества с числами и выполните над ними операции объединения, пересечения и разности.
set_first = {1,2,3,4,5,6,7}
set_twist = {5,6,7,8,9,10,4}

set_new_unification = set_first.union(set_twist)
print('Объединенное множество:', set_new_unification)

set_new_intersection = set_first & set_twist
print('Пересечение множеств:', set_new_intersection)

set_new_difference = set_first - set_twist
print('Разность множеств:', set_new_difference)

set_simm_difference= set_first ^ set_twist
print('Симметричная разность множеств:', set_simm_difference)
