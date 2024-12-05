import re

FILTER_PAT = r"mul[(]{1}[0-9]+,{1}[0-9]+[)]{1}"
NUMS_PAT = r"[0-9]+,[0-9]+"
DO_PAT = r"do[(]{1}[)]{1}"
DONT_PAT = r"don't[(]{1}[)]{1}"

with open('example2.txt', 'r') as f:
    all = []
    for x in f:
        all.append(re.findall(FILTER_PAT, x))
        all.append(re.findall(DO_PAT, x)[0])
        all.append(re.findall(DONT_PAT, x)[0])

    print(all)
