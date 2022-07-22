# модуль для оптимизации ошибок при вводе данных

def try_input(n, lst1):
    counter = 0
    while n not in lst1:
        if n == '0':
            return
        counter += 1
        if counter < 3:
            n = input("Введите корректные данные: ").title()
            print("Данные введены некорректно.")
        else:
            n = input("""Для выхода в главное меню нажмите '0'. Введите корректные данные: """).title()
            print("Данные введены некорректно.")
    return n


def zero_error(x):
    if x == 0:
        exit()
