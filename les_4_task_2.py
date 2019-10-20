
__author__ = 'AlexNik'

# Задача: 1. Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_4_task_1, les_4_task_2, и т.д.
# Для оценки «Отлично» необходимо выполнить оба задания.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2


import timeit
import cProfile

# Решето Эратосфена
def sieve_(num):
    num_list = [i for i in range(num)]
    num_list[1] = 0

    for j in range(2, num):
        if num_list[j] != 0:
            k = j + j
            while k < num:
                num_list[k] = 0
                k += j

    res = [i for i in num_list if i != 0]
    return res

def sieve(num):
    first_num = {1: 2, 2: 3}
    if num in first_num:
        return first_num[num]

    num_list = sieve_(num)
    counter = num
    while len(num_list) < num:
        counter += num_list[-1]
        num_list = sieve_(counter)
    res = num_list[num - 1]
    return res


s = """
def sieve_(num):
    num_list = [i for i in range(num)]
    num_list[1] = 0

    for j in range(2, num):
        if num_list[j] != 0:
            k = j + j
            while k < num:
                num_list[k] = 0
                k += j

    res = [i for i in num_list if i != 0]
    return res

def sieve(num):
    first_num = {1: 2, 2: 3}
    if num in first_num:
        return first_num[num]

    num_list = sieve_(num)
    counter = num
    while len(num_list) < num:
        counter += num_list[-1]
        num_list = sieve_(counter)
    res = num_list[num - 1]
    return res
    
sieve(10000)
"""

#print(timeit.timeit(s, number=100))
# 0.23354970000000003 = 20
# 0.014321999999999998 = 40
# 0.0305768 = 80
# 0.08550559999999999 = 160
# 0.23354970000000003 = 500
# 0.4861964 = 1000
# 13.1471239 = 10000

#cProfile.run('sieve(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.116    0.116 <string>:1(<module>)
#         5    0.092    0.018    0.113    0.023 les_4_task_2.py:30(sieve_)
#         5    0.013    0.003    0.013    0.003 les_4_task_2.py:31(<listcomp>)
#         5    0.009    0.002    0.009    0.002 les_4_task_2.py:41(<listcomp>)
#         1    0.001    0.001    0.115    0.115 les_4_task_2.py:44(sieve)
#         1    0.000    0.000    0.116    0.116 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ______________________________________________________________________________________________________________________
# Без решета Эратосфена:
def check(n):
    i = 2
    j = 0
    while i * i <= n and j != 1:
        if n % i == 0:
            j = 1
        i = i + 1
    if j == 1:
        pass
    else:
        return n

def prime(num):
    num_list = [2, 3]
    if num == 1 or num == 2:
        return num_list[num - 1]
    i = 3
    while True:
        i += 1
        if check(i) == None:
            pass
        else:
            num_list.append(i)
            if len(num_list) == num:
                return num_list[-1]


s_2 = """
def check(n):
    i = 2
    j = 0
    while i * i <= n and j != 1:
        if n % i == 0:
            j = 1
        i = i + 1
    if j == 1:
        pass
    else:
        return n

def prime(num):
    num_list = [2, 3]
    i = 3
    while True:
        i += 1
        if check(i) == None:
            pass
        else:
            num_list.append(i)
            if len(num_list) == num:
                return num_list[-1]

prime(10000)
"""

#print(timeit.timeit(s_2, number=100))
# 0.0040251 = 20
# 0.011870400000000003 = 40
# 0.0355919 = 80
# 0.0961209 = 160
# 0.4936799 = 500
# 1.5062602999999999 = 1000
# 46.3712384 = 10000

#cProfile.run('prime(10000)')
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.476    0.476 <string>:1(<module>)
#    104726    0.448    0.000    0.448    0.000 les_4_task_2.py:112(check)
#         1    0.026    0.026    0.475    0.475 les_4_task_2.py:124(prime)
#         1    0.000    0.000    0.476    0.476 {built-in method builtins.exec}
#      9998    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      9998    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: поочередная проверка каждого числа замедляет процесс при поиске больших простых чисел

# ______________________________________________________________________________________________________________________
# Проверка:
def control_check(n):
    print(sieve_(1000))
    if n > len(sieve_(1000)):
        return 'Максимальное число проверки = 168'
    print(sieve(n))
    print(prime(n))
#control_check(168)