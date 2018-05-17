import re
import sys

for line in sys.stdin:
    line = re.sub(r"\ba+\b", "argh", line.rstrip(), count = 1, flags = re.IGNORECASE)
    print(line) 
