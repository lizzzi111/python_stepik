import re
import sys

for line in sys.stdin:
    line = re.sub("human", "computer", line.strip())
    print(line)
