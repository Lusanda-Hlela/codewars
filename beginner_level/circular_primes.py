def circular_prime(n):
    if n <= 10000 and n > 1:
        n = str(n)
        numbers = list()
        for i in n:
            numbers.append(i)

        circular_numbers = list()
        for i in range(len(numbers)):
            n = numbers.copy()
            arr = n[i:] + n[:i]
            circular_numbers.append(arr)

        primes = list()
        for i in circular_numbers:
            i = int(''.join(i))
            for j in range(2, i):
                remainder = (i % j)
                if remainder == 0:
                    break
            else:
                primes.append(i)

        if len(primes) == len(circular_numbers):
            return True
        else:
            return False
    else:
        return False