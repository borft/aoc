from aoc import input

def is_fresh(ranges: list[list, int], ingredient: int) -> bool:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            return True
    return False

def overlapping(r1: list[int], r2: list[int]) -> list[list[int]]:
    # the + and - 1 are for the edge case where ranges are not overlapping, but one
    # continuous range can be made, e.g. 1-2 and 3-4 would become 1-4
    if r1[1] < r2[0] -1 or r1[0] > r2[1] + 1:
        # no overlap
        return [r1, r2]

    if r2[0] <= r1[0]:
        start = r2[0]
    else:
        start = r1[0]
    if r1[1] <= r2[1]:
        end = r2[1]
    else:
        end = r1[1]

    return [[start, end]]

# first parse input
ranges = []
fresh = []
for line in input(1):
    t =  line.split('-')
    if len(t) == 2:
        # this is a range
        ranges.append([int(i) for i in t])
    elif len(line) == 0:
        # this is the empty line, loading of ranges complete, let's order and calculate non overlapping
        ranges.sort()

        while True:
            non_overlapping = []

            for r in ranges:
                if len(non_overlapping) == 0:
                    # first iteration, cannot be overlap
                    non_overlapping.append(r)
                else:
                    for index, no in enumerate(non_overlapping):
                        t = overlapping(r, no)
                        if len(t) == 1:
                            # overlapping, otherwise there'd be 2 ranges
                            non_overlapping[index] = t[0]
                            break
                    else:
                        non_overlapping.append(r)

            if ranges == non_overlapping:
                # if there are no more changes, there are no more overlapping ranges
                break
            else:
                ranges = non_overlapping
    elif len(line) > 0:
        # this line contains an ingredient, let's check if it's fresh
        if is_fresh(ranges, int(line)):
            fresh.append(line)


print(f'count: {len(ranges)} -- {ranges}')
print(f'fresh: {len(fresh)}')

# wrong: 339668510830774
# right: 339668510830757
count = 0
for no in non_overlapping:
    count += no[1] - no[0] +1
print(f'{count} - {non_overlapping}')

