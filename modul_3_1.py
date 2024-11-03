
# Пространство имён

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    result = len(string), str.upper(string), str.lower(string)
    return result

def  is_contains(string, list_to_search):
    count_calls()
    string = str(string).upper()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).upper() == string:
            result = True
            break
        else:
            result = False
    return result

print(string_info('Denis'))
print(string_info('Vegetable'))
print(string_info('Airplane'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
