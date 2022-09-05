dict_type_table = {1: 'Разрешения на строительство',
                               2: 'Разрешения на ввод'}

print(dict_type_table.get(3))

if dict_type_table.get(3):
    print('2222')