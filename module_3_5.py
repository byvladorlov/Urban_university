def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if (int(str_number[len(str_number)-1])) == 0: #проверка окончания числа на 0
        str_number = str_number.strip('0') #убираем 0 в конце
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
