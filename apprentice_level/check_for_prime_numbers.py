def is_prime(n):
    primes = list()
    if n < 2:
        return False
    else:
        for i in range(2, n):
            prime = n % i
            primes.append(prime)
    
    if 0 in primes:
        return False
    else:
        return True