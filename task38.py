# Меню
def show_menu():
    print("\nВыбери пункт меню, введя соответствующую команду:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по имени\n"
          "3. Найти абонента по фамилии\n"
          "4. Найти абонента по номеру телефона\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить абонента из справочника\n"
          "7. Изменить данные абонента в справочнике\n"
          "8. Сохранить справочник в текстовом формате\n"
          "9. Закончить работу")
    option = int(input())
    return option

# Трансформация 
def parse_cvs(filename):
    columns= []
    rows = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(rows, line.strip().split(',')))
            columns.append(record)
    return columns

#Все функции 
def phonebook_functions():
    option = show_menu()
    phonebook = parse_cvs('phonebook.csv')

    while (option !=9):
        if option == 1:
           about_phonebook(phonebook)
        elif option == 2:
            about_phonebook(search_by_name(phonebook))
        elif option == 3:
           about_phonebook(search_by_surname(phonebook))
        elif option == 4:
            about_phonebook(search_by_number(phonebook))
        elif option == 5:
            add_new_user(phonebook)
            add_to_cvs('phonebook.csv', phonebook)
        elif option == 6:
            remove_user(phonebook)
            rewrite_to_cvs('phonebook.csv', phonebook)
        elif option == 8:
            save_list()
        option = show_menu()

# 1. Отображение справочника
def about_phonebook(phonebook):
    for elem in phonebook:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print()            

# 2. Поиск по имени
def search_by_name(phonebook):
    name = input('Введите имя для поиска: ')
    output = []
    for elem in phonebook:
        if elem['Имя'] == name:
            output.append(elem)
    return output
                                             
# 3. Поиск по фамилии
def search_by_surname(phonebook):
    surname = input('Введите фамилию для поиска: ')
    output = []
    for elem in phonebook:
        if elem['Фамилия'] == surname:
            output.append(elem)
    return output

# 4. Поиск по номеру телефона
def search_by_number(phonebook):
    number = input('Введите номер телефона пользователя: ')
    output = []
    for elem in phonebook:
        if elem['Телефон'] == number:
            output.append(elem)
    return output

# 5. Добавить нового абонента
def add_new_user(phonebook):
    record = dict()
    for u in phonebook[0].keys():
        record[u] = input(f'Введите {u}: ')
    phonebook.append(record)

def add_to_cvs(filename, phonebook):
    with open(filename, 'a', encoding='utf-8') as data:
        line = ''
        for i in phonebook[-1].values():
            line += i + ','
        data.write(f'{line[:-1]}\n')

# 6. Удаление абонента
def remove_user(phonebook):
    user = input('Введите фамилию или имя абонента для удаления: ')
    for elem in phonebook:
        for i in elem.values():
            if i == user:
                phonebook.remove(elem)

def rewrite_to_cvs(filename, phonebook):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in range(len(phonebook)):
            line = ' '
            for i in phonebook[i].values():
                line += i + ','
            data.write(f'{line[:-1]}\n')

# 7. Изменение данных
def change_user_info(phonebook):
    user = input('Введите фимилию или имя для изменения:') 
    changed_data = input('Введите данные: ')    
    new_data = input('Введите новое значение данных: ')
    for elem in phonebook:
        for i in elem.values():
            if i == user:
                elem[changed_data] = elem[changed_data].replace(elem[changed_data],new_data)

# 8. Сохранение текста
def save_list():
    filename = input('Введите имя файла для сохранения: ')
    shutil.copyfile('phonebook.csv',f'{filename}.txt')

# 9. Закончить работу cо справочником
import shutil
phonebook_functions()                           

