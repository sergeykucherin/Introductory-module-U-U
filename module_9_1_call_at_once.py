
def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results [function.__name__] = function(int_list)
    return results

def min_list(int_list):
    return min(int_list)

def max_list(int_list):
    return max(int_list)

def len_list(int_list):
    return len(int_list)

def sum_list(int_list):
    res = 0
    for i in int_list:
        res += i
    return res

def sorted_list(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
