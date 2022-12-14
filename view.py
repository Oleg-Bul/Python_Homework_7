def cont_to_search():
    """Поиск контактов"""
    search_entered = input('Введите фамилию контакта: ')
    return search_entered


def show_contacts(to_search, result):
    """Вывод фамилии и номера контакта """
    print('Номер вашего контакта - ', to_search, ':', result)


def added_contact(to_search):
    """Предлагает добавить несуществующий контакт"""
    print('Данного контакта не сущеествует в списке!')
    new_number = input(f'Если желаете добавить новый контакт - введите\
номер контакта "{to_search}": ')
    return new_number


def contact_write(to_search, new_contact):
    """Уведомляет о добавлении контакта в справочник"""
    print(f'Контакт "{to_search}" c номером "{new_contact}" добавлен в файл')
