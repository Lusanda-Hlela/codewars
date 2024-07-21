def remove_duplicate_words(s):
    s = s.split()
    d = dict()
    for i in s:
        v = s.count(i)
        d[i] = v
    
    k = str()
    for i in d:
        k += i
        k += ' '
    
    k = k.strip()
    return k