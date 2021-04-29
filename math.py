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
    print("Помилка")