
__author__ = 'AlexNik'

# Задача: 3. Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские
# имена, например, les_3_task_1, les_3_task_2 и т.д.
# Для оценки «Отлично» достаточно выполнить 4 любых задания на ваш выбор («Отлично» ставится
# за работы без ошибок).
# Например, если вы сдадите 7 заданий и 3 из них сделаны неверно, оценка не может быть отличной.

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted
# и их аналогов, в том числе написанных самостоятельно.

import random


SIZE = 50
MIN_ITEM = 2
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')

num_min = array[0]
num_min_ind = 0
num_max = array[0]
num_max_ind = 0
for i in range(0, len(array)):
    if num_min > array[i]:
        num_min = array[i]
        num_min_ind = i
    elif num_max < array[i]:
        num_max = array[i]
        num_max_ind = i
array[num_max_ind] = num_min
array[num_min_ind] = num_max
print(f'{array}\nВыполнена замена элементов с индексами {num_min_ind} и {num_max_ind}')
