from module2 import Student_with_additional_inf 
from module3 import Container         
from module5 import try_input
group1 = Container()
list_group1 = []


def add_object():
    x = input("Введите фамилию и имя студента, которого хотите добавить в список: ").title()
    group1.group_append(x)
    print(f"Студент {x} добавлен в список")
    x = Student_with_additional_inf(x)
    list_group1.append(x)


def edit_object():
    print("""
    Доступные функции:
    1.Добавить возраст студента.
    2.Добавить пол студента.
    3.Добавить семейное положение студента
        """)
    show_group()
    name1 = try_input(input("Введите фамилию и имя студента: ").title(), group1.group)
    func1 = try_input(input("\nВведите номер функции: "), ("1", "2", "3"))
    if func1 == "1":
        age1 = try_input(input("Введите возраст студента: "), list(map(str, range(15,75))))
        list_group1[group1.group.index(name1)].input_age(age1)
        print(f"Добавлен возраст студента {name1}")
    elif func1 == "2":
        gender1 = try_input(input("Введите пол студента (М/Ж): "), ("М", "Ж"))
        list_group1[group1.group.index(name1)].input_gender(gender1) 
        print(f"Добавлен пол студента {name1}")
    elif func1 == "3":
        status1 = try_input(input("Введите семейное положение студента (Женат/Не женат): ").title(), ("Женат", "Не женат"))
        list_group1[group1.group.index(name1)].input_status(status1) 
        print(f"Добавлен семейный статус студента {name1}")


def remove_object():
    if len(group1.group)>0:
        show_group()
        delname = try_input(input("Введите фамилию и имя студента, которого нужно удалить из списка: ").title(), group1.group) 
        del_index = group1.group.index(delname)
        del group1.group[del_index]
        del list_group1[del_index]
        print(f"Студент {delname} удален из списка")
    else:
        print("Список пуст")


def show_group():
    if len(group1.group)>0:
        print("Полный список студентов:")
        group1.group_print()
    else:
        print("Список пуст")


def save_in_file():
    file1 = input("Введите имя файла для внесения данных: ")
    group1.group_write_file(file1)
    print(f"Данные были сохранены в файл {file1}")


def download():
    x = input("Введите имя файла для получения данных: ")
    try:
        group1.group_read_file(x)
        print(f"Данные, взятые из файла {x}:")
        group1.group_print()
    except FileNotFoundError:
        print("Такого файла не существует.")
        download()


def object_inform():
    show_group()
    name1 = try_input(input("Введите фамилию и имя студента: ").title(), group1.group)
    list_group1[group1.group.index(name1)].print_age()
    list_group1[group1.group.index(name1)].print_gender()
    list_group1[group1.group.index(name1)].print_status()


def stop():
    print("Баг с отсутствием выхода ещё не пофиксили :) сорри ГЫ-ГЫ")


def main():
    print("""
        Меню функций:
        1. Добавить объект
        2. Редактировать объект
        3. Удалить объект
        4. Вывести на экран весь список
        5. Сохранить в файл
        6. Загрузить из файла
        7. Вывести полную информацию о студенте
        0. Выйти из приложения
          """)
    func_menu = {"1": add_object,
            "2": edit_object,
            "3": remove_object,
            "4": show_group,
            "5": save_in_file,
            "6": download,
            "7": object_inform,
            "0": stop
            }
    n = try_input(input("\nВведите номер функции: "), func_menu)
    func_menu[n]()

