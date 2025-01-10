def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n > 1:
            if all((n % i != 0) for i in range(2, int(n ** 0.5) + 1)):
                res = "Простое"
            else:
                res = "Составное"
        print(res)
        return n
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)


