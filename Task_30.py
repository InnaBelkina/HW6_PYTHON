# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию

# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:

# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, 
# в одну строку, вам понадобится распаковка и Comprehension или map

def arithmetic_progression(a,d,n):
    result_list= []
    a_1=a
    while a <= (a_1 + (n-1) * d):
        result_list.append(a)
        a+=d
    return result_list

def arithmetic_progression_2(a,d,n):
    result_list=[]
    for i in range (n):
        result_list.append(a)
        a+=d
    return result_list

def arithmetic_progression_3(a,d,n):
    result_list= []
    for i in range (a,(a + (n-1) * d)+1,d):
        result_list.append(i)
    return result_list

a = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите шаг: "))
n = int(input("Введите количество элементов: "))

print(arithmetic_progression(a,d,n))
print(arithmetic_progression_2(a,d,n))
print(arithmetic_progression_3(a,d,n))

# Усложнение (*)
def arithmetic_progression_comprehension(a,d,n):
    return [i for i in range(a,(a + (n-1) * d)+1,d)]

print(arithmetic_progression_comprehension(a,d,n))

# P.S. Пока искала решение для comprehension получилось написать несколько вариантов для простого решения задачи. Решила оставить все. Извините, если отняла много лишнего времени.

