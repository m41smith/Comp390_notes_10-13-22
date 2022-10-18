def add(t1, t2):
    print(f'{t1} + {t2} = {t1+t2}')


def test():
    list_types = ['bob', None, True, ['Tom', 34, False], 86]
    print(add(list_types[3][1], list_types[4]))

    count = 0
    while count < 12:
        print(f'this is iteration {count}')
        count = count + 1

    try:
        return add(34, 68)
    except Exception as error:
        print('An error has occured')
        return
    finally:
        print('you tried to add two numbers')


def dicts():
    npc_dict = {'type': 'monster',
                'hp': 100,
                'exp': 1000}
    print({npc_dict['type']})

    for key, value in npc_dict.items():
        print(f'{key}: {value}')


('''CREATE TABLE IF NOT EXISTS filtered_data(
                name TEXT
                id INTEGER),''')

