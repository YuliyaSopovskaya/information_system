


import read
import set_get
import logger


def seek_emp():
    job_title = set_get.set_job_title()
    employees = read.read_csv()
    print('*'*80)
    for index,item in enumerate(employees):
        if item == job_title:
            emp = employees[index-3:index+3]
            print_emp(emp)
    
    return emp

def seek_emp_surname():
    employees = read.read_csv()
    surname = set_get.set_surname()
    emp = []
    for index,item in enumerate(employees):
        if item == surname:
            emp =emp + employees[index:index+6]
    return emp



def print_emp(emp: list):
    print('*'*80)
    emp = " ".join(emp).split()
    headers = ['Фамилия','Имя','д.р.','должность','разряд','оклад']
    print(f'{headers[0]:<15} {headers[1]:<10} {headers[2]:11} {headers[3]:<10} {headers[4]:<6} {headers[5]:<6}')
    print(f'{emp[0]:<15} {emp[1]:<10} {emp[2]:11} {emp[3]:<10} {emp[4]:<6} {emp[5]:<6}')
    

def edit_employees():
    emp = seek_emp_surname()
    emp = (" ".join(emp)).split()
    print('*'*80)
    headers = ['Фамилия','Имя','д.р.','должность','разряд','оклад']
    print(f'{headers[0]:<15} {headers[1]:<10} {headers[2]:11} {headers[3]:<10} {headers[4]:<6} {headers[5]:<6}')
    for i in range(0, len(emp)-1, 6):
        print(f'{emp[i]:<15} {emp[i+1]:<10} {emp[i+2]:11} {emp[i+3]:<10} {emp[i+4]:<6} {emp[i+5]:<6}')

    if len(emp)>6:
        surname = emp[0]
        name = set_get.set_name()
    else:
        surname = emp[0]
        name = emp[1]
    while True:
        
        employees = read.read_csv()
        for index,item in enumerate(employees):
            if surname == item and name == employees[index+1]:  
                            
                i = index
                z = input('Вы уверены? 1/0 да/нет ')
                if z == '1':
                    break
        break
    n = input('что меняем ? \n1. фамилию. \n2. имя\n3. д.р. \n4. должность \n5. разряд \n6. оклад \n')
    match n:
        case '1': 
            employees[i] = set_get.set_surname()
            change = 'фамилия'
        case '2': 
            employees[i+1] = set_get.set_name()
            change = 'имя'
        case '3': 
            employees[i+2] = set_get.set_borndate()
            change = 'д.р.'
        case '4':
            employees[i+3] = set_get.set_job_title()
            change = 'должность'
        case '5':
            employees[i+4] = set_get.set_rank()
            employees[i+5] = str(int(set_get.get_salary(emp)) * 1.05 )    
            change = 'разряд и оклад'
        case '6':
            employees[i+5] = set_get.set_salary()        
            chenge = 'оклад'
    txt_msg = ('внесены изменения ')+change +' '+ surname+' ' + name
    logger.number_logger(txt_msg)
    return employees
