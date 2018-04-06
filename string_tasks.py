s, a, b = [input().strip() for _ in range(3)]
#s = "ababa"
#a = "c"
#b = "c"
cnt = 0
if s.find(a)==-1:
    print(cnt)
elif b.find(a)!=-1:
        print('Impossible')
else:
    while s.find(a)!=-1:
        s = s.replace(a,b)
        cnt += 1
    print(cnt)
