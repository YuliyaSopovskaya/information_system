import Edit
import csv
import read
import set_get
import logger

def new_employee():
    emp = []
    
    emp.append(set_get.set_surname())
    emp.append(set_get.set_name())
    emp.append(set_get.set_borndate())
    emp.append(set_get.set_job_title())
    emp.append(set_get.set_rank())
    emp.append(set_get.set_salary())
    txt_msg ='добавлен сотрудник '+ emp[0] +' '+ emp[1]
    logger.number_logger(txt_msg)
    return emp

def delete_employee():
    employees = read.read_csv()
    emp = Edit.seek_emp_surname()
    print('*'*80)
    headers = ['Фамилия','Имя','д.р.','должность','разряд','оклад']
    print(f'{headers[0]:<15} {headers[1]:<10} {headers[2]:11} {headers[3]:<10} {headers[4]:<6} {headers[5]:<6}')
    for i in range(0, len(emp)-1, 6):
        print(f'{emp[i]:<15} {emp[i+1]:<10} {emp[i+2]:11} {emp[i+3]:<10} {emp[i+4]:<6} {emp[i+5]:<6}')
    surname = emp[0]
    if len(emp)>6:
        name = set_get.set_name()
    else:
        name = emp[1]
    for index,item in enumerate(employees):
            if surname == item and name == employees[index+1]:  
                txt_msg = 'удален сотрудник '+surname +' '+name
                z = input('Вы уверены? 1/0 да/нет ')
                if z == '1':
                    for j in range(0,6):
                        employees.pop(index)      
    
    logger.number_logger(txt_msg)
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(employees)


