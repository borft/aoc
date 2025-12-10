from aoc import input


lights = []
buttons = []
joltages = []
for line in input():
    parts = line.split(' ')
    b = []
    for part in parts:
        if part[0] == '[':
            light = []
            for c in part[1:-1]:
                if c =='#':
                    state = True
                else:
                    state = False
                light.append(state)
            lights.append(light)
        elif part[0] == '(':
            b.append([int(i) for i in part[1:-1].split(',')])
        elif part[0]  == '{':
            joltages.append([int(i) for i in part[1:-1].split(',')])

    buttons.append(b)

print(lights)
print(buttons)
print(joltages)

count = len(lights)

def get_combos(options, combos):
    ret = []
    for o in options:
        for c in combos:
            t = c.copy()
            t.append(o)

            ret.append(t)
    return ret


def check(light: list, combination) -> bool:
    state = [False] * len(light)

    for c in combination:
        if c[1] == 0:
            continue
        else:
            for b in c[0]:
                state[b] = not state[b]
   # print(f'light: {light} - state: {state}')
    return state == light



results = []
for i in range(0, count):


    l = lights[i]
    button = buttons[i]

    print(f'trying {i} / {len(button)}')

    combinations = []

    for b in button:
        options = []
        for j in [0,1]:
            options.append([b,j])
        if len(combinations) == 0:
            combinations = [[o] for o in options]
        else:
            combinations = get_combos(options, combinations)



    pressed_count = len(button)
    for c in combinations:
        if check(l, c):
            print(f'yay: {l} / {c}')
            # calculate buttons pressed
            pressed_count = min(sum([1 for cc in c if cc[1] == 1]), pressed_count)
    results.append(pressed_count)

print(f'{sum(results)} --> {results}')

