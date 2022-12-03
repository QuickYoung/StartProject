print ('Калькулятор')
continue = 'c'
while continue == 'c':
    f_num = float(input('Введите первое число:'))
    oper = input('Введите операцию:')
    s_num = float(input('Введите второе число:'))
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print ('Error')
continue = input('Чтобы продолжить, напишите "C"')        
