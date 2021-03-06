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

n = N
for p in generator_of_primes():
    while n % p == 0:
        if n <= p:
            break
        n = n / p
    if n <= p:
        print n
        break