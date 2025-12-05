from aoc import input


# build matrix
m = []
for line in input():
    m.append(line)

height = len(m)
width = len(m[0])


def check_cell(m: list[list[str]], height: int, width: int) -> int:
    d = [-1, 0, 1]
    
    maxheight = len(m)
    maxwidth = len(m[0])
    
    free = 0
    for hc in d:
        for wc in d:
            if hc == 0 and wc == 0:
                continue
            h = height + hc
            w = width + wc
            # print(f'checking ({hc}:{wc}) {h}:{w} from {height}:{width}')

            if 0 <= h < maxheight and 0 <= w < maxwidth:
                if m[h][w] == '.':
                    free += 1
            else:
                print(f'not checking')
                free += 1
    print(f'checked {height}, {width} --> {free} ')
    return free
    

total_free = 0
while True:
    start = total_free
    for i in range(0, height):
        for j in range(0,width):
            #print(f'cell {i},{j} -> {m[i][j]}')

            if m[i][j] == '.':
                continue

            free = check_cell(m, i, j)
            if free > 4:
                total_free += 1
                print(f'replacing {i}:{j} {m[i][j]} in {m[i]}')
                t = m[i][:j] + '.' 
                if j <= width: 
                    t += m[i][j+1:]
                m[i] = t
                
                print(f'new: {m[i]}')
                
                
    print(f'found: {total_free}')
    if start == total_free:
        break;
