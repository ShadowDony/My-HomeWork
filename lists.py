# Необходимо создать функцию, которая будет генерировать список (list) самостоятельно в псевдослучайном порядке.
# Функция должна обладать аргументами, которые будут ограничивать длину списка, а также максимальное цифровое значение элементов этого списка.
# Например:
# Сегнерировать список из 10 чисел, каждое из которых может быть в диапазоне от 1 до 9.

import random

def renlists():
    listLength = int(input("Введіть довжину списку -> "))
    maxVal = int(input("Введіть максимальне цифрове значення елементів списку -> "))

    data = [random.randint(0, maxVal) for i in range(0, listLength )]
    print(data)
    return renlists()
renlists()