def prime_factorization(number: int) -> list:
    prime_factor = 2
    primes = []

    for num in range(number + 1):
        if number % prime_factor == 0:
            primes.append(prime_factor)
            number /= prime_factor
        else:
            prime_factor += 1

    return primes


def find_primes_factor(number: int) -> list:
    counter = 2
    primes = []

    while number != 1:
        if number % counter == 0:
            primes.append(counter)
            number /= counter
        else:
            counter += 1

    return primes