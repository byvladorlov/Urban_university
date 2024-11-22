calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_tuple = (len(string), string.upper(), string.lower())
    return str_tuple

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    return any(string in i.lower() for i in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) #No matches
print(calls)

