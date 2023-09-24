'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''


def main(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('r - Просмотреть все контакты\nw - Добавить контакт\ns - Найти контакт\nq - Выйти из '
                            'приложения\n')
        print()
        if user_choice == 'r':
            show_phonebook(phonebook)
        elif user_choice == 'w':
            add_phone_number(phonebook)
        elif user_choice == 's':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == 'q':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона (11 символов): '))
            if len(str(phone_number)) != 11:
                print('Неправильно введен номер')
            else:
                flag = True
        except ValueError:
            print('Недействительный номер')
    return last_name, first_name, str(phone_number)


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value} ', end='')
        print()


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


main('phonebook.txt')