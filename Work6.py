# # 1 Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

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