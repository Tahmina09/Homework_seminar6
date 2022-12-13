# Семинар 3 задача 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

l = int(input('Введите длину списка: '))

my_list = [i + 1 for i in range(l)]
print(my_list)

def find_and_sum(a_list: list):
    sum_index = 0
    for i in range(len(a_list)):
        if i % 2 != 0:
            sum_index += a_list[i]
    print(sum_index)

find_and_sum(my_list)