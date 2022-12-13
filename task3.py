# Семинар 2 задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

number = float(input('Введите вещественное число: '))

number = str(number)
temp = number.replace('.' , '')

res = [int(k) for k in temp]
print(res)

print(sum(res))