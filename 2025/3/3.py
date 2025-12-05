from aoc import input


def find_right_and_lower(source: list, res: list, limit: int, old: int, new: int):

    # pos
    pos = min([p for (p,v) in res])
    #limit = min([v for (p,v) in res])

    print(f'pos: {pos} for {limit} // {res} len: {len(res)}')

    ret = {}
    for i in range(old, new, -1):

        value = source[i]
        if value < limit:
            if not value in ret:
                ret[value] = []
            ret[value].append(i)
    return ret




jolts = []

jolts_b = []
for line in input():
#for line in ['4343335344372513234535342343343331535336323543354634443324332253537437441345145433453334416434323352']:
    digits = [int(c) for c in line]

    #print(f'got line {line} // {digits}')

    first = max(digits[:-1])
    last = 0
    found = False

    for d in digits:
        if d == first and not found:
            found = True
            continue

        if not found:
            continue
        if d > last:
            last = d
    # print(f'{line} :: {first}{last}')
    jolts.append(int(f'{first}{last}'))


    res = []
    for i in range(9, 0, -1):
        if len(res) == 12:
            break

        start = len(digits)-1
        if len(res) > 0:
            start = min([p for (p,v) in res])
            print(f'setting start to {start} with {len(digits)}')
            old_min_pos = min([p for (p,v) in res])
        else:
            old_min_pos = len(digits) -1

        # look to the left
        new_pos = []
        for j in range(start, -1, -1):
            d = digits[j]
            print(f'looking at {i}::{j} / {d} - {d==i}')
            if d == i:
                res.append((j, d))
                new_pos.append(j)

            if len(res) == 12:
                break



        # if more than 1 have been added, do multiple backfills
        for np in sorted(new_pos, reverse=True):

            if len(res) > 0 and len(res) < 12:

                #new_min_pos = min([p for (p,v) in res])
                new_min_pos = np
                print(f' backfill from {old_min_pos} to {new_min_pos}')
                # now (back)fill from the right
                right = find_right_and_lower(digits, res, i, old_min_pos, new_min_pos)
                print(right)
                for value in sorted(right.keys(), reverse=True):
                    positions = right[value]
                    for p in positions:
                        print(f'adding {value}@{p}')
                        res.append((p, value))
                        if len(res) == 12:
                            break
                    if len(res) == 12:
                        break
                print(right)
                print(res)

        if len(res) == 12:
            break


    s = int(''.join([str(v) for (p,v)  in sorted(res, key=lambda item:item[0])]))

    print(f'len:{len(res)} : {s} ::  {line} : {max(digits)} : {max(digits) == int(str(s)[0])} : {str(max(digits)) in str(s)} ')
    jolts_b.append(s)


## wrong: 166387542069505
##        166826564803805
##        167979662154930

    print(f'found {res} based on {line} / {digits}')
    #break


print(f'count: {len(jolts)} - jolts: {jolts}')
print(sum(jolts))

print(jolts_b)
print(sum(jolts_b))
