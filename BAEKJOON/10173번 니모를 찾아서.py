import re

while True:
    sen=input()
    if sen=='EOI': break
    p=re.findall('.nemo.',sen.lower())
    if len(p)!=0: print("Found")
    else: print("Missing")