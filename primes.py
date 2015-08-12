N = 600851475143


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

for i in generator_of_primes():
    if i > N / 2:
        break
    if N % i == 0:
        print 'Prime factor is', i