import sys
data = {}
exs = []
for_output = []
def find_ancestor(ex, target_ancestor):
    global data
    for ancestor in data[ex]:
        if ancestor == target_ancestor:
            return True
        elif find_ancestor(ancestor, target_ancestor):
            return True
        else:
            continue
    return False

def read_user_input(file_name):
    global data, exs, for_output
    if file_name:
        inf = open(file_name)
    else:
        inf = sys.stdin

    n = int(inf.readline())
    while n > 0:
        line = inf.readline().rstrip()
        if ':' in line:
            ex, ancestry = map(str, line.split(':'))
            ex = ex.rstrip()
            ancestors = ancestry.strip().split(' ')
        else:
            ex = line
            ancestors = []
        if ex not in data:
            data[ex] = []
        data[ex].extend(ancestors)
        n -= 1

    m = int(inf.readline())
    exs = []
    while m > 0:
        ex = inf.readline().rstrip()
        exs.append(ex)
        for_output.append(False)
        m -= 1
    for i in range(0, len(exs)):
        for j in range(i, len(exs)):
            if i == j:
                continue
            elif find_ancestor(exs[j], exs[i]):
                for_output[j] = True

for i in range(0, len(exs)):
    if for_output[i]:
        print(exs[i])
