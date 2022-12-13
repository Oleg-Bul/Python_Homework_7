def choose_mode():
    """Запрос выбора игры"""
    mode = ''
    print('Для игры в крестики-нолики - введите "1"')
    print('Для игры в конфеты - введите "2"')
    x = int(input('Выберите игру: '))
    if 0 < x and x < 3:
        if x == 1:
            mode = 'Крестики нолики'
            print('Вы выбрали игру: Крестики нолики ')
        elif x == 2:
            mode = 'Конфеты'
            print('Вы выбрали игру: Конфеты')
    else:
        print('Введите число 1 или 2')
    return mode


def show_results(result):
    """Вывод результатов игры"""
    if result == 1:
        print('Победил игрок 1')
    elif result == 2:
        print('Победил игрок 2')
    elif result == 0:
        print('Ничья')
    else:
        print('Ошибка')
    print(result)
