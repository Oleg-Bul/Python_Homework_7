def get_base():
    with open('contacts.txt', encoding='utf-8') as file:
        lines = file.read().splitlines()
    base = {}
    for line in lines:
        key, value = line.split('//')
        base.update({key: value})
    return base


def added_number(to_search, new_contact):
    with open('contacts.txt') as f:
        read_data = f.read()
    with open('contacts.txt', 'w') as f:
        f.write(to_search + "//" + new_contact + '\n' + read_data)
