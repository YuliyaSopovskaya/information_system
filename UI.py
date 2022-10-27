


import Edit
import write
import read
import add_delete


def menu():
    read.write_csv()
    while True:
        z = input(
            "Введите 1 - посмотреть список сотрудников. \nВведите 2 - поиск сотрудника по фамилии. \nВведите 3 - поиск по должности. \nВведите 4 - обновить данные сотрудника. \nВведите 5 - удалить (уволить) сотрудника. \nВведите 6 - добавить сотрудника.\nВведите 0 - выход.\n")
        match z:
            case '1':
                read.print_employees()
                print()
            case '2':
                Edit.seek_emp_surname()
                print()
            case '3':
                Edit.seek_emp()
                print()
            case '4':
                write.write_employees()
                print()
            case '5':
                add_delete.delete_employee()
                print()
            case '6':
                write.write_employees_new()
            case '0':
                break