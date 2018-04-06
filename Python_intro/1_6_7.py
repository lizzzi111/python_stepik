data = {}

def findAncestor(clazz, targetAncestor):
    global data
    for ancestor in data[clazz]:
        if ancestor == targetAncestor:
            return True
        elif findAncestor(ancestor, targetAncestor):
            return True
        else:
            continue
    return False

n = int(input())
while n > 0:
    line = input().rstrip()
    if ':' in line:
        clas, ancestry = map(str, line.split(':'))
        clas = clas.rstrip()
        ancestors = ancestry.strip().split(' ')
    else:
        clas = line
        ancestors = []
    if not clas in data:
        data[clas] = []
    data[clas].extend(ancestors)
    n -= 1

q = int(input())
while q > 0:
    maybeAncestor, clas = map(str, input().split())
    if (maybeAncestor == clas) or findAncestor(clas, maybeAncestor):
        print('Yes')
    else:
        print('No')
    q -= 1
