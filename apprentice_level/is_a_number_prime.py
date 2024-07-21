def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        e = int((num**0.5) + 1)
        if e > 2:
            for i in range(2, e):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return True