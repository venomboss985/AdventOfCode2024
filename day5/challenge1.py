with open('input.txt', 'r') as f:
    challenge: list = [[], []]
    idx: int = 0
    for x in f:
        if x == '\n':
            idx = 1
            continue
        x = x.replace('\n', '')
        if idx == 0:
            x = x.split('|')
        # else:
        #     x = x.split(',')
        challenge[idx].append(x)

    ref: dict = {}
    for z in challenge[0]:
        x = z[0]
        y = z[1]
        if ref.get(x) == None:
            ref[x] = []
        ref[x].append(y)

    total: int = 0
    for z in challenge[1]:
        print('-'*15)
        z = z.split(',')
        print(z)

        cache: str = ""
        invalid: bool = False
        for k in z:
            before = []
            try:
                before = ref[k]
            except:
                pass

            for b in before:
               if str(b) in cache:
                invalid = True

            cache += k + ','
        print('inv:', invalid)

        if not invalid:
            mid_page = len(z) // 2
            total += int(z[mid_page])
            print("mid_page:", z[mid_page])

    print("T:", total)
