numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count = 0
for i in range(len(numbers)):
    is_prime = True
    x = numbers[i]
    if x < 2:
        continue
    else:
        y = x ** 0.5
    for j in range(2, int(y + 1)):
        if x % j == 0:
            is_prime = False
            break
        count += 1
    if not (is_prime):
        not_primes.append(x)
    else:
        primes.append(x)
print(primes)
print(not_primes)

