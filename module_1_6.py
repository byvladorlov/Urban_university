my_dict = {'Vlad': 1998, 'Sasha': 1997, 'Nikita': 1991, 'Olga': 1977, 'Vika': 2005}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Sasha'))
print('Not existing value: ', my_dict.get('Oleg','Такой ключ отсутствует'))
my_dict.update({'Oleg': 1965, 'Katya': 1985})
a = my_dict.pop('Nikita')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
print('\n')
my_set = {'Apple', 'Samsung', 33, 1, 'Lenovo', 17, 'Samsung', 17, 3, 'Apple',2,33,'Apple',1}
print('Set:', my_set)
my_set.update({'Xiaomi', 303})
my_set.remove('Lenovo')
print('Modified set: ', my_set)