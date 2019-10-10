
__author__ = 'AlexNik'

# Задача: 1. Написать программу, которая будет складывать,
# вычитать, умножать или делить два числа. Числа и знак
# операции вводятся пользователем. После выполнения вычисления
# программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при
# вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), программа
# должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления
# на ноль, если он ввел его в качестве делителя.

# Примечания:
# 1. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
# 2. Попытайтесь решить задания без использования массивов в любых вариациях (массивы будут рассмотрены на следующем уроке). Для простоты понимания любые квадратные скобки [ и ] считаются массивами и их наличие в коде расценивается как неверное решение.
# 3. Как минимум одна задача должна быть решена с помощью рекурсии.

# Реализация без функции
operator = 1
while operator != '0':
    operator = str(input("Какое действие желаете произвести"
                      " ('+', '-', '*', '/', 0 - для выхода)?"))

    while operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '0':
            operator = str(input("ОШИБКА ВВОДА!\nКакое действие желаете произвести"
                      " ('+', '-', '*', '/', 0 - для выхода)?"))
    if operator == '0':
        print('Good luck!')
    else:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if operator == "/":
            while b == 0:
                b = int(input("На 0 делить нельзя\nВведите число b: "))
            print(a, ' / ', b, ' = ', a / b)
        elif operator == "*":
            print(a, ' * ', b, ' = ', a * b)
        elif operator == "+":
            print(a, ' + ', b, ' = ', a + b)
        else:
            print(a, ' - ', b, ' = ', a - b)
