numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

num = 0
for i in range(2, len(numbers) + 1):
    for j in range(2, i):
        if i % j == 0:
            num = num+ 1
    if num == 0:
        primes.append(i)
    else:
        num = 0
        not_primes.append(i)
print('primes:', primes)
print('not_primes:', not_primes)

