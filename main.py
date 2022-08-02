# Создать информационную систему позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы

database = {}
db = {'parents': 1, 'children': 2}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))


def find_relatives_tel(telephone):
    t = [i for i in database[db['parents']] if telephone in i]
    if t == []:
        id = [i[1] for i in database[db['children']] if telephone in i][0]
        tel = [j[3] for j in database[db['parents']] if id == j[0]]
        print("Parent's telephone: " + str(*tel))
    else:
        id = [i[0] for i in database[db['parents']] if telephone in i][0]
        tel = [j[5] for j in database[db['children']] if id == j[1]]
        if tel != []:
            print("Children's telephones: " + str(' '.join(tel)))
        else:
            print('Not have relatives')

# Найти телефоны остальных членов семьи (если они есть) по номеру телефона.
reading_file_to_dict(1)
reading_file_to_dict(2)
find_relatives_tel('89483332255')



def print_children(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])



# Создать решение для вывода детей по фамилии
# print_children('Ivanov')

