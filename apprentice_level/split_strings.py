def solution(s):
    if (len(s) % 2) == 0:
        l = []
        while s:
            l.append(s[:2])
            s = s[2:]
        return l
    else:
        s = s + '_'
        l = []
        while s:
            l.append(s[:2])
            s = s[2:]
        return l