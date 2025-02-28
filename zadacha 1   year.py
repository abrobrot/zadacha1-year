def is_year_leap (year: int):
    visokosnyi = True
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        visokosnyi = True
        print(visokosnyi)
    else:
        visokosnyi = False
        print(visokosnyi)

year=(int(input('Введите год: ')))
is_year_leap(year)