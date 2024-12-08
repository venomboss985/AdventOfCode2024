with open('input.txt', 'r') as f:
    cal: int = 0

    for x in f:
        x = x.replace('\n', '')

        val, expr = x.split(':')
        expr = expr[1:].split(' ')
        perms: int = 2 ** (len(expr))

        for perm in range(perms):
            total: int = 0

            for i, num in zip(range(len(expr)), expr):
                num = int(num)
                mask: int = 2**i
                op: str = '*' if perm & mask else '+'

                if op == '+' or i == 0: total += num
                if op == '*': total *= num

            if total == int(val):
                cal += total
                break

    print('Cal:', cal)
