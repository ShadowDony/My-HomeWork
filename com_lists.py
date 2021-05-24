#Необходимо написать функцию, которая будет брать два случайно сгенерированных списка (задача №7) и сравнивать их между собой.

#Уникальные числа (которые есть только в одном списке) выводить в консоль с любым комментарием.
import random

def com_lists():
    list_length1 = int(input("Введіть довжину списку №1 -> "))
    max_val_list1 = int(input("Введіть максимальне цифрове значення елементів списку №1 -> "))
    list_length2 = int(input("Введіть довжину списку №2 -> "))
    max_val_list2 = int(input("Введіть максимальне цифрове значення елементів списку №2 -> "))

    data_list1 = [random.randint(0, max_val_list1) for i in range(0, list_length1)]
    data_list2 = [random.randint(0, max_val_list2) for i in range(0, list_length2)]

    print("Список1 -", data_list1, "Список2 -", data_list2)

    if data_list1 == data_list2:
        print("Списки співпали")
    else:
        res_lists = list(set(data_list1) ^ set(data_list2))
        print("Унікальні числа -", res_lists)

    return com_lists()
com_lists()