def generator_of_primes():
    a = 3
    primes = [3]
    yield 2
    yield 3
    while True:
        a += 2
        is_prime = True
        for i in primes:
            if (a + 1) / 2 < i:
                break
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(a)
            yield a

for i, prime in enumerate(generator_of_primes(), 1):
    if i == 10001:
        print prime
        break
