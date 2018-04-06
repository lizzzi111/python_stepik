def cnt(s, t):
    n = 0
    if t in s:
        for i in range(len(s)):
            if s[i:].startswith(t):
                n += 1
    return n

s, t = input(), input()
#s = "abababa"
#t = "aba"
print(cnt(s, t))
