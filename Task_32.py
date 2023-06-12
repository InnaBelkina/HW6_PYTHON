# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному .
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

def idx(list, min, max):
    result_list=[]
    for i in range(len(list)):
        if list[i] >= min and list[i]<=max:
            result_list.append(i)
    return result_list

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min=int(input("Задайте минимум диапазона: "))
max=int(input("Задайте максимум диапазона: "))
print(idx(list,min,max))

# # При повторяющихся числах не меняет индекс на новый
# def idx_2(list, min, max):
#     result_list=[]
#     for i in list:
#         if i in range(min,max+1):
#             result_list.append(list.index(i))
#     return result_list
# print(idx_2(list,min,max))

# Усложнение (*)

def idx_comprehension(list, min, max):
    return [i for i in range(len(list)) if list[i] >= min and list[i]<=max]

print(idx_comprehension(list,min,max))

# Усложнение 2(*). 
def idx_tuple(list, min, max):
    result_list=[]
    for i,v in enumerate(list):
        if v >= min and v<=max:
            result_list.append((i,v))
    return result_list

print(idx_tuple(list,min,max))