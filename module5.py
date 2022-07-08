#модуль для оптимизации ошибок при вводе данных

def try_input(n, lst1):
    if n not in lst1:
        print("Данные введены некорректно.")
        return try_input(input("Введите корректные данные: "), lst1)
    return n


