from csv import DictReader, DictWriter
from os.path import exists
file_name = 'phone.csv'
new_file_name = 'new_phone.csv'

def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else :
                flag = True
        except ValueError:
            print('Невалидный номер')
        
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)
    
def standart_write(file_name, lst):
    res = read_file(file_name)
    res.append(lst)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def write_file(file_name, lst):
    obj = {'Имя' :lst[0], 'Фамилия':lst[1], 'Телефон':lst[2]}
    standart_write(file_name, obj)

def copy_row(file_name = file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        lst_1 = []
        for row in f_r:
            lst_1.append(row)
        flag = False
        while not flag:
            number = int(input("Введите номер строки: "))
            if number > len(lst_1):
                    print(f"Превышено колличество строк. Всего строк({len(lst_1)}.)")
            else:
                flag = True
        if not exists(new_file_name):
            create_file(new_file_name)
        standart_write(new_file_name, lst_1[number-1])


def main():
    while True:
        command = input("Введите команду: ")
        if command=='q':
            break
        elif command =="w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_row(file_name)

main()
