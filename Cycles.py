import math
'''Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
Ввод пользователя должен осуществляться с помощью input.
Если пользователь вводит ноль, то выводиться на экран среднее значение.
Используйте цикл while для решения данной задачи'''

# lst = []
# summ = 0
# total = 0
# num = int(input('Введите числа (после ввода "0" программа завершит свою работу): '))
# while num != 0:
#     try:
#         summ += num
#         total += 1
#         lst.append(num)
#         num = int(input('Введите числа (после ввода "0" программа завершит свою работу): '))
#     except ValueError:
#         print('Введите только числа!')
# if total > 0:
#     Average_number = summ / total
#     print(f'Среднее арифметическое: {Average_number}')
# else:
#     print('Вы не ввели ни одного числа.')
'''Напишите программу для вывода на экран чисел от 0 до 100
Вам понадобиться цикл for, конструкция range и print'''
# for i in range(1, 101):
#     print(i)
'''Напишите программу для вывода таблицы умножения от 0 до 9.
Используйте вложенный цикл for, print и range'''
# for i in range(1, 10):
#     for j in range(1, 10,):
#         print(i,'*', j, '=', (i*j), end='\t')
#     print()
'''Создайте список с разными значениями,
пройдитесь по нему в цикле и выведите на экран.
(Сделайте тоже самое со словарем и выведите ключ и значение)'''
# my_list = [1, 'hello', 5.8, True, 'world']
# print('Элементы списка:')
# for i in my_list:
#     print(i, end=', ')
'''Словарь'''
# mi_dict = {'один': 1, 'привет': 'hello', 'Истина': True}
# for key, value in mi_dict.items():
#     print(f'Ключ: {key}, Значение: {value}')
'''Вывести все числа от 1 до 100, которые делятся на 3 без остатка.'''
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)
'''Найти сумму всех чисел от 1 до 100.'''
# total = 0
# for i in range(1, 101):
#     total += i
# print(f'Сумма всех чисел от 1 до 100: {total}')
'''Вывести таблицу умножения для числа 2 от 1 до 10.'''
# num = 2
# for i in range(1, 11):
#     print(num, '*', i, '=', 2*i)
'''Найти все простые числа от 2 до 50.'''
# for i in range(2, 51):
#     osn = True
#     for j in range(2, i):
#         if i % j == 0:
#             osn = False
#             break
#     if osn and i != 0:
#         print(i, end=',')
'''Посчитать сумму квадратов чисел от 1 до 10.'''
# summ = sum([x ** 2 for x in range(1, 11)])
# print(f'Сумма квадратов: {summ}')
'''Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.'''
# for x in range(1, 20, 1):
#     x /= 2
#     y = x**2
#     print(f'x = {x}, y = {y}')
'''Найти факториалы чисел от 1 до 5 (включительно).'''
# factors = [math.factorial(i) for i in range(1, 6)]
# print(', '.join(map(str, factors)))