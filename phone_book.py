# Написать псевдо-телефонную книгу

def create_contact():
    '''Contact creation(создание контакта)'''

    surname = input('Введите фамилию: ').title()
    name = input('Введите имя: ').title()
    patronymic = input('Введите отчество: ').title()
    phone = input('Введите номер телефона: ')
    address = input('Введите адрес(город): ').title()

    return f'{surname} {name} {patronymic}\n{phone}\n{address}\n\n'
    

def write_contact():
    '''File creation and add contact(создание файла и добавление контакта)'''

    contact = create_contact()
    
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contact}')
        print('\nКонтакт записан!\n')


def print_contacts():
    '''Сontact output(вывод контактов)'''

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    
    for nn, contact in enumerate(contacts_list, 1):
        print(f'{nn}. {contact}\n')


def search_contact(field=''):
    '''Contact search(поиск контакта)'''
    
    print(
    'Возможные варианты поиска:\n'
    '1. по фамилии\n'
    '2. по имени\n'
    '3. по отчеству\n'
    '4. по номеру\n'
    '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1

    search = input('Введите данные для поиска: ').title()

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')
    
    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')


def copy_contact(): 
    '''Contact copying(копирование контакта)'''

    print_contacts()
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().split('\n\n')

    index = int(input('Введите номер контакта, который необходимо скопировать: '))-1

    with open('contacts.txt', 'a', encoding='utf-8') as file:
        file.write(contacts_list[index])
        print('\nКонтакт скопирован!\n')


def delete_contact():
    '''Contact deletion(удаление контакта)'''

    print_contacts()

    new_list = []

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().split('\n\n')
    
    index = int(input('Введите номер контакта, который необходимо удалить: '))-1
        
    for line in range(len(contacts_list)):
        if line != index:
            new_list.append(contacts_list[line])

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(new_list))

        print('\nКонтакт удалён!\n')


# def edit_contact():
#     '''Edit a contact(редактировать контакт)'''

#     print_contacts()

#     new_contact = []
#     index = int(input('Введите номер контакта, который необходимо редактировать: '))-1

#     print(
#         '1. Изменить имя'
#         '2. Изменить фамилию'
#         '3. Изменить отчество'
#         '4. Изменить номер'
#         '5. Изменить адрес'
#         )

#     change_row = input('Введите номер строки, которую необходимо редактировать: ')

#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         contacts_list = file.read().split('\n\n')

#     for line in range(len(contacts_list)):
#         if line == index:


def __main__():
    
    with open('phonebook.txt', 'a'):
        pass

    user_input = None

    while user_input != '7':

        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Удалить контакт\n'
            '6. Изменить контакт\n'
            '7. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                delete_contact()
            # case '6':
                # edit_contact()

if __name__ == '__main__':
    __main__()