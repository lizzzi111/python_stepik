import re
import sys

ff = "this is a text"
ff2 = "this' !is. ?n1ce"
for line in sys.stdin:
    new_line = []
    for word in line.split():
        if len(word)>=2:
            word = re.sub(r"\b(\w)(\w)", r"\2\1", word)
            new_line.append(word)
        else:
            new_line.append(word)
    print(" ".join(new_line))
