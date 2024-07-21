def new_avg(arr, newavg):
    import math
    n = sum(arr)
    d = len(arr)
    if d > 0:
        avg = n / d
        if avg != newavg:
            i = newavg * (d + 1) - avg * d
            if i > 0:
                return math.ceil(i)
            else:
                raise ValueError
        else:
            raise ValueError
    elif d == 0:
        return newavg
    else:
        raise ValueError