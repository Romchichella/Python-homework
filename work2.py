# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:

# # - 6782 -> 23
# # - 0,56 -> 11


# a = input('Введите число: ')
# sum = 0
# for i in a:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



# a = int(input('Введите число: '))
# step = 1
# sum = 1

# if a < 0:
#     a = -a

# while step < a+1:
#     sum *= step
#     print(sum, end=" ")
#     step += 1

# # 3 Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

# n = int(input('Введите число: '))
# step = 1
# sum = 0

# while step < n+1:
#     sum = sum + (1 + 1/step)**step
#     step += 1
# print(round(sum, 2))

