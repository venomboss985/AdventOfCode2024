# Advent of Code Day 1 - Puzzle 1

with open('input.txt', 'r') as f:
    sim: int = 0
    left: list = []
    right: list = []

    for x in f:
        x = x.replace('\n', '').split('   ')
        left.append(int(x[0]))
        right.append(int(x[1]))

    for i in left:
        freq = right.count(i)
        sim += i * freq

    print("S:", sim)
