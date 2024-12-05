from copy import copy

with open('example.txt', 'r') as f:
    safe = 0
    for x in f:
        x = x.replace('\n', '').split(' ')
        temp = []
        for i in x:
            temp.append(int(i))
        x = copy(temp)

        print('-'*10)
        valid = []
        UP = 9
        DOWN = 36
        SAME = 22
        for i in range(len(x)):
            if i+1 >= len(x): break
            initial = x[i]
            next = x[i+1]

            # Check if out of range
            if ((initial < next + 3 or initial > next - 3) and (initial < next + 1 or initial > next - 1)):
                # Check if up
                if (initial < next):
                    valid.append(UP)

                # Check if down
                if (initial > next):
                    valid.append(DOWN)

                # Check if same
                if (initial == next):
                    valid.append(SAME)

            # print("init:", initial, "next:", next)

        value = sum(valid)
        print("x:", x)
        print("valid:", valid)
        # print("value:", value)
        if (value == valid[0] * (len(x)-1)):
            print("This row is valid")
