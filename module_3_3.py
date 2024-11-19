#1.Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params('test')
print_params(33, b = False)
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров
values_list = ['Basic', True, 17.03]
values_dict = {'a':'Pascal', 'b': 52, 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры
values_list_2 = [True, 20.24]
print_params(*values_list_2, 42)
