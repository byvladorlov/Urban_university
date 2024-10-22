immutable_var = tuple([21, 'May', 1998, ['Slava','Orlov'], 17.5, True])
print(immutable_var)
#immutable_var[0] = 22 /данное значение изменить нельзя, так как оно находится в кортеже, который относится к неизменяемым типам данных и не поддерживает обращение к элементам.
immutable_var[3][0] = 'Vlad' #но несмотря на неизменяемость самого кортежа, в себе он может хранить какие-то изменяемые объекты, в данном случае список
print(immutable_var)
print('\n')
mutable_list = [22, 'May', 1998, 'Slava', 'Olrov', 17.5, False]
print(mutable_list)
mutable_list[0] = 21
mutable_list[3] = 'Vlad'
mutable_list.insert(-1,True)
mutable_list.remove(False)
print(mutable_list)