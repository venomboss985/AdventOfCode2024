#!/usr/bin python3
# Advent of Code Day 1 - Puzzle 1

with open('input.txt', 'r') as f:
    dist: int = 0
    left: list = []
    right: list = []

    for x in f:
        x = x.replace('\n', '').split('   ')
        left.append(int(x[0]))
        right.append(int(x[1]))

    left.sort()
    right.sort()

    for x, y in zip(left, right):
        dist += abs(x - y)

    print("D:", dist)
