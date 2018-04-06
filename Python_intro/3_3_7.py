import sys
import pandas as pd

for line in sys.stdin:
    line = line.rstrip()
    if pd.Series(line).str.contains("cat.*cat")[0]:
        print(line)


## Better solution
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
