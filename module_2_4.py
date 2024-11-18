numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(1,i):
        if numbers[i]%numbers[j] == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)
