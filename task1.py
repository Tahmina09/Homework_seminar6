# Семинар 2 задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. 
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

num = int (input ('Введите число: '))

n_list = list(range(-num, num + 1))
print(n_list)
   
print()

intered_index = input( ' Введите индексы чисел для произведения: ').split()
index_list = list (map (int, intered_index))
print('Список индексов: ', index_list)

multi = 1
for k in range(len(index_list)):
    multi *= n_list[index_list[k]]
    k += 1
print('Вывод:', multi) 