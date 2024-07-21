def high(x):
    '''List on alphabets'''
    alphabets = list()
    for i in range(ord('a'), ord('z') + 1):
        i = chr(i)
        alphabets.append(i)
    
    '''List of scores per alphabets'''
    numbers = list()
    for i in range(1, 27):
        numbers.append(i)
    
    '''Dictionary of alphabets as keys, and scores as values'''
    d = dict()
    for key in alphabets:
        for value in numbers:
            d[key] = value
            numbers.remove(value)
            break
    
    '''Find the length of each word'''
    l = list()
    for i in x.split():
        length = len(i)
        l.append(length)
    
    '''Create a list of scores for each letter in the string'''
    scores = list()
    for i in x.split():
        for j in i:
            s = d[j]
            scores.append(s)

    '''Create a list of total scores for each word
    Use the word length to perform the task'''
    ts = list()
    for i in l:
        w = scores[:i]
        s = sum(w)
        ts.append(s)
        scores = scores[i:]
        s = 0
    
    '''Create a dictionary, keys = words, values = total score of the word'''
    database = dict()
    for i in x.split():
        for j in ts:
            database[i] = j
            ts.remove(j)
            break
    
    '''Return the results to the function call'''
    return max(database, key = lambda k: database[k])