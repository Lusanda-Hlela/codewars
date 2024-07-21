def binary_array_to_number(arr):
    l = len(arr)
    base = 2
    s = list()
    i = l - 1
    while i >= 0:
        d = base ** i
        i -= 1
        s.append(d)
        
    zeroes = list()
    for k in range(l):
        if arr[k] == 0:
            zeroes.append(k)
    
    for j in zeroes:
        s[j] = 0
    
    sum = 0
    for x in s:
        sum += x
    return sum