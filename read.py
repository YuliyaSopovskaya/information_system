


import csv


def write_csv():
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
                 'Фамилия','Имя','д.р.','должность','разряд', 'оклад',
                 'Иванов','Иван', '23.03.1988', 'Рабочий', '3', '15000',
                 'Васильев','Дмитрий', '22.12.1989', 'Рабочий', '3', '15000',
                 'Петров'   ,'Василий', '16.12.1978', 'Рабочий', '4', '17000',
                 'Иванов','Петр', '03.06.1998', 'Рабочий', '3', '15000',
                 'Карасев', 'Карп', '13.04.1979', 'Мастер', 'нет', '25000',
                 'Путин'  , 'Вова', '02.05.1980', 'Директор', 'нет', '55000'                 
                 ])
        

def read_csv():
    with open('names.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        for row in reader:
            s = ', '.join(row)
        employees = s.split(',')
        return employees

        
def print_employees():
    print('*'*100)
    employees = read_csv()
    count = 0
    for i in range(0,len(employees),6):
        emp = ' '.join(employees[i:i+6])
        emp = emp.split()
        print(f'{count}. {emp[0]:<15} {emp[1]:<10} {emp[2]:11} {emp[3]:<10} {emp[4]:<6} {emp[5]:<6}')
        count += 1
    print('*'*100)