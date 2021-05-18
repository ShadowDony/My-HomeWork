def calculate():
    f_num = float(input("Введіть перше значення >>> "))
    oper = input("Введіть операцію (+,-,*,/) >>>")
    s_num = float(input("Введіть друге значення >>> "))
    if oper == '+':
        print("Результат дорівніює >>>", (f_num + s_num))
    elif oper == '-':
        print("Результат дорівніює >>>", (f_num - s_num))
    elif oper == '*':
        print("Результат дорівніює >>>", (f_num * s_num))
    elif oper == '/':
        print("Результат дорівніює >>>", (f_num / s_num))
    else:
        print("Помилка. Введіть правильний оператор")
    again()
def again():
    calc_again = input('''
    Бажаєте знову відкрити калькулятор?
    Натисніть Y для "ТАК" чи N для "НІ".
    ''')
    if calc_again.upper() == 'Y':
       calculate()
    elif calc_again.upper() == 'N':
        print('До побачення.')
    else:
        again()
calculate()