import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"z\w{3}z", line):
        print(line)
