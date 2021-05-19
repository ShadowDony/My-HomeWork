def comparison():
    a = input("Введіть значення A -> ")
    b = input("Введіть значення B -> ")

    if a > b:
        print ("Успішно")
    elif a == b:
        print ("Майже")
    else:
        print ("Лузер")

    return comparison()
comparison()