numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for x in numbers:
    for y in range(2,x):
        if x % y == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True and x != 1:
        primes.append(x)
    elif x != 1:
        not_primes.append(x)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')