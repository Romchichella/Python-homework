# 1. Напишите программу, которая принимает на
# # вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет
# print('Введите число от 1 до 7')
# den = int(input())
# if den == 6 or den == 7:
#     print('Этот день - выходной')
#     if den==6:
#         print('А если быть точнее - суббота')
#     elif den==7:
#         print('А если быть точнее - воскресенье, и завтра на работу')
# else:
#     print('Вы ввели будний день')
#     print()
#     if den == 1:
#         print('А если быть точнее - понедельник')
#     elif den==2:
#         print('А если быть точнее - вторник')
#     elif den==3:
#         print('А если быть точнее - среда')
#     elif den==4:
#         print('А если быть точнее - четверг')
#     elif den==5:
#         print('Почти повезло, сегодня - пятница')
# print()

# 2. Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


# print ('Введите число Х')
# X3 = bool(input())
# print ('Введите число Y')
# Y3 = bool(input())
# print ('Введите число Z')
# Z3 = bool(input()) 
# if not (X3 or Y3 or Z3) == (not X3 and not Y3 and not Z3): 
#     print ('Выражение истинно')
# else:
#     print('Выражение ложно')
# print()

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input('Введите значение по оси x: '))
y = int(input('Введите значение по оси y: '))

if(x==0 and y==0):
    print('Оба значения не могут быть равны нулю')
elif(x==0):
    print('Точка лежит на оси y, плоскость определить невозможно')
elif(y==0):
    print('Точка лежит на оси x, плоскость определить невозможно')
elif(x>0 and y>0):
    print('1')
elif(x>0 and y<0):
    print('4')
elif(x<0 and y>0):
    print('2')
elif(x<0 and y<0):
    print('3')

    