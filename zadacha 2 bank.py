def bank (year,a):
    i=0
    while i < year:
        a = a*1.1
        i +=1
    print(a)
year=(int(input('Введите срок в годах: ')))
a=(int(input('Введите сумму: ')))
bank(a,year)