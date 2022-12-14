# 1 Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# # список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# # список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# # список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# # список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# # список: [], ищем: "123", ответ: -1

# from typing import List

# def show_second_index(input_list: List[str], trigger_str: str) -> int:
   
#     print(input_list)
#     index_lst = [i for i, string in enumerate(
#         input_list) if trigger_str == string]
#     try:
#         return (f'позиция второго вхождения строки в список: {index_lst[1]}')
#     except IndexError:
#         return 'такой строки в списке нет, либо встречается только 1 раз'


# input_list = list((input('Ввести элементы списка через пробел\n')).split(' '))
# trigger_str = input('Ввести искомую строку с маленькой буквы\n')
# print(show_second_index(input_list, trigger_str))

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from functions import give_int, random_list
# from typing import List


# def pair_mult(data_list: List[int]) -> List[int]:
#     '''
#     Gives multiplication of elements on opposite indexes
#     :param data_list: list with elements
#     :return: list with multiplication of elements on opposite indexes
#     '''

#     return [data_list[i]*data_list[-1 - i] for i in range(len(data_list)//2 + len(data_list) % 2)]


# dt_lst = random_list(4)
# print(dt_lst)
# res = pair_mult(dt_lst)
# print(res)

# dt_lst = random_list(5)
# print(dt_lst)
# res = pair_mult(dt_lst)
# print(res)

# 3 Сформировать список из N членов последовательности.
# # Для N = 5: 1, -3, 9, -27, 81 и т.д.

# from functions import give_int

# result = [(-3)**i for i in range(give_int('Type amount of numbers: '))]
# print(result)

# 4 Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

# from functions import create_random_list


# def sum_of_digits(number):
#     sum = 0
#     while number > 0:
#         sum = sum + (number % 10)
#         number = number//10
#     return sum


# lst = create_random_list(10, 100)
# print(lst)

# result = [i for i in lst if not sum_of_digits(i) % 2]
# print(result)

# 5 Есть список случайных чисел в промежутке от 1 до 200, количеством 200.
# Создайте список кортежей, первый элемент которого - индекс элемента,
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

# # 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# # Пример
# # [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

# from functions import create_random_list
# from typing import List


# def check_coincidence(i) -> bool:
    
#     t1, t2 = i
#     if t1 == t2:
#         return False
#     else:
#         return True


# def check_multiple_5(i) -> bool:
   
#     t1, t2 = i
#     if (t1 + t2) % 5:
#         return False
#     else:
#         return True


# lst = create_random_list(1, 10)
# print(lst)

# tuples_lst = list(enumerate(lst))
# print(tuples_lst)

# result1 = list(filter(check_coincidence, tuples_lst))
# print(result1)

# result2 = list(filter(check_multiple_5, result1))
# print(result2)