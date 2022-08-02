# Создать базу данных телефонов из имеющихся данных(тел.; Имя; Фамилия)

tel_base = []

def get_tel_base(number_file):
    with open(f'{number_file}.txt', 'r') as f:
        data = [i.split('\n')[0] for i in f.readlines()]
        for i in data:
            tel_base.append(tuple(i.split(';')))

def make_tel_base(data):
    with open('3.txt','a') as tel:
        for i in data:
            tel.write(''.join(i[-1]) +';' + ';'.join(i[1:3]) + '\n')

get_tel_base(1)
make_tel_base(tel_base)
tel_base = []
get_tel_base(2)
tel_base = [tel_base[i] for i in range(1, len(tel_base))]
tel_base = [i[1:] for i in tel_base]
make_tel_base(tel_base)
            