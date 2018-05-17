import re
import sys

ff = "attraction"
ff2 = "buzzzz"
for line in sys.stdin:
    new_line = []
    for word in line.split():
        if len(word)>=2:
            word = re.sub(r"((\w)\2*)", r"\2", word)
            new_line.append(word)
        else:
            new_line.append(word)
    print(" ".join(new_line))
