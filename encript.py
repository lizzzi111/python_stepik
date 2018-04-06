from simplecrypt import encrypt, decrypt
import pandas as pd

folder = "/Users/lizzzi111/Downloads"
with open(f"{folder}/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
passwords = pd.read_table(f"{folder}/passwords.txt", header=None)
passwords[0]
for i in passwords[0]:
    try:
        print(decrypt(i, encrypted))
    except:
        pass
