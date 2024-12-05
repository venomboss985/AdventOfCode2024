import re

FILTER_PAT = r"mul[(]{1}[0-9]+,{1}[0-9]+[)]{1}"
NUMS_PAT = r"[0-9]+,[0-9]+"

with open('input.txt', 'r') as f:
    muls = []
    for x in f:
        for y in re.findall(FILTER_PAT, x):
            muls.append(re.findall(NUMS_PAT, y)[0])

    total = 0
    for x in muls:
        mult = x.split(',')
        mult = [int(mult[0]), int(mult[1])]
        total += mult[0] * mult[1]

    print("T:", total)
