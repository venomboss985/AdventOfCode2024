with open('example.txt', 'r') as f:
    cal: int = 0

    for x in f:
        x = x.replace('\n', '')

        val, expr = x.split(':')
        expr = expr[1:].split(' ')
        perms: int = 3 ** (len(expr))

        for perm in range(perms):
            total: int = 0
            print('P:', perm)

            for i, num in zip(range(len(expr)), expr):
                num = int(num)
                mask: int = 3<<i*2
                op: str = ""
                c_perm: int = perm*3

                masked = c_perm & mask
                perm_str: str = "0"
                for c in range(masked):
                    masked = masked>>1
                    if bin(masked)[-1] == '1' or bin(masked)[-2] == 'b':
                        perm_str = bin(masked)[2:]
                        break

                test: int = 2 if int(perm_str) == 11 else int(perm_str)

                if test == 0: op = '+'
                if test == 1: op = '*'
                if test == 2: op = '||'

                print(bin(c_perm)[2:], bin(mask)[2:], bin(test)[2:], op)

                if   op == '+' or i == 0: total += num
                elif op == '*': total *= num
                elif op == '||': total = int(str(total) + str(num))

            print(total)
            print()

            if total == int(val):
                cal += total
                break

    print('Cal:', cal)
