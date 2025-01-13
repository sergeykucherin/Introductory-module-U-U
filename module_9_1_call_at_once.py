
def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results [function.__name__] = function(int_list)
    return results

def min(int_list):
    min_ = int_list[0]
    for i in int_list:
        if i <= min_:
            min_ = i
    return min_

def max(int_list):
    max_ = int_list[0]
    for i in int_list:
        if i >= max_:
            max_ = i
    return max_

def len(int_list):
    counter = 0
    for i in int_list:
        counter +=1
    return counter
#
def sum(int_list):
    res = 0
    for i in int_list:
        res += i
    return res

def sorted(int_list):
    for i in range(1, len(int_list)):
        j = int_list[i]
        while (int_list[i - 1] > j and i > 0):
            int_list[i] = int_list[i - 1]
            i -= 1
            int_list[i] = j
    return int_list

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

