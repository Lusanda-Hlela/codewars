def anagrams(word, words):
    w = sorted(word)
    l = list()
    for i in words:
        s = sorted(i)
        if w == s:
            l.append(i)
        else:
            l = l
    return l