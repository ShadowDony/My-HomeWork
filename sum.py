def suma_chysel():
    n = int(input("Введіть число -> "))
    suma = 0
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    print("Сума:", suma)
    return suma_chysel()
suma_chysel()