import os
from datetime import datetime as dt


def log_result(i, result):
    event_dt = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    if (os.path.isfile('results.csv')):
        id = sum(1 for line in open('results.csv', 'r'))
    else:
        id = 0 
    with open('results.csv', 'a') as file:
        file.write('{};{};Игра:{};Победитель:{}\n'.format(id, event_dt, i, result))
    return "Результат игры записан в файл."
