


import Edit
import add_delete
import csv
import read
import logger

# запись справочника
def write_employees_new():
    emp = add_delete.new_employee()
    employees = read.read_csv()
    employees = employees + emp
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(employees)



def write_employees():
    employees = Edit.edit_employees()
    txt_msg = 'перезаписан список сотрудников '
    logger.number_logger(txt_msg)
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(employees)