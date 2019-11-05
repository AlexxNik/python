
__author__ = 'AlexNik'

#1. Для каждого упражнения написать программную реализацию.
#Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские
# имена, например les_8_task_1, les_8_task_2, и т.д.
#Для оценки «Отлично» необходимо выполнить одно любое задание.

#2) Закодируйте любую строку по алгоритму Хаффмана.

# сортировка
def bubble_sort(array, reverse=False):
    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array[1]):
        is_sorted = True
        for i in range (len(array[1]) - n):
            if array[1][i] * sign < array[1][i + 1] * sign:
                array[1][i], array[1][i + 1] = array[1][i + 1], array[1][i]
                array[0][i], array[0][i + 1] = array[0][i + 1], array[0][i]
                is_sorted = False
        if is_sorted:
            break
        n += 1

# получаем структуру
def d_haffman(haf_dict):
    j = -1
    haf_matrix = [[0] * len(haf_dict) for _ in range(2)]
    haf_dict = dict(sorted(haf_dict.items(), key = lambda k: k[1]))
    for i in haf_dict:
        haf_matrix[0][j] = i
        haf_matrix[1][j] = haf_dict[i]
        j -= 1

    check_count = 0
    while check_count - 2 > j:
        bubble_sort(haf_matrix, reverse=True)
        haf_matrix[0][check_count-2] = (haf_matrix[0][check_count-1], haf_matrix[0][check_count-2])
        haf_matrix[1][check_count-2] = (haf_matrix[1][check_count-1] + haf_matrix[1][check_count-2])
        check_count -= 1
    return tuple(haf_matrix[0][0])

# получаем словарь по ранее найденной структуре
def haf_code(haf_tuple, h_code={}):
    if len(haf_tuple) == 1:
        return h_code
    if h_code == {}:
        h_code[tuple(haf_tuple)] = ''
    h_code[haf_tuple[0]] = ''.join(h_code[haf_tuple]) + "0"
    h_code[haf_tuple[1]] = ''.join(h_code[haf_tuple]) + "1"
    haf_code(haf_tuple[0], h_code)
    haf_code(haf_tuple[1], h_code)
    return h_code


test_word = ['beep boop beer!']
if len(test_word[0]) == 1:
    print(f'{test_word}: 0')
else:
    haf_dict = {}
    for i in test_word[0]:
        if i in haf_dict:
            haf_dict[i] += 1
        else:
            haf_dict[i] = 1
    print(f'Результат кодирования фразы {test_word} \n алгоритмом Хаффмана: {d_haffman(haf_dict)}')
    h_code = haf_code(d_haffman(haf_dict))
    for i in test_word[0]:
        print(f'{i}: {h_code[i]}')

#Отличный курс! Спасибо за качественный подход к обучению, было интересно!