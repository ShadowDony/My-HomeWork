def com():
    a = int(input("Введіть значення A -> "))
    b = int(input("Введіть значення Б -> "))
    c = int(input("Введіть значення В -> "))
    while a <= b:
        a = a + c
        print("А = A + В =", a)
    else:
        print("Вийшло, таки A =",a, "і тому більше за Б")
com()
