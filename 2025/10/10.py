from aoc import input
import math


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

def get_combos(options: list[list[object]], combos: list[list[list]]) -> list[list[list]]:
    ret = []
    for o in options:
        for c in combos:
            t = c.copy()
            if o[1] > 0:
                t.append(o)


            ret.append(t)
    print(f'sizeofcombo: {len(ret)}')
    return ret


def get_combos2(options: list[list[object]], combos):
#    ret = []
    for o in options:
        for c in combos:
            t = c.copy()
            if o[1] > 0:
                t.append(o)


            yield t
    #         ret.append(t)
    # print(f'sizeofcombo: {len(ret)}')
    # return ret


def check_light(light: list, combination) -> bool:
    state = [False] * len(light)

    for c in combination:
        if c[1] == 0:
            continue
        else:
            for b in c[0]:
                state[b] = not state[b]
   # print(f'light: {light} - state: {state}')
    return state == light


part1 = False

if part1:
    results = []
    for i in range(0, count):


        l = lights[i]
        button = buttons[i]

        print(f'trying {i} / {len(button)}')

        #combinations: list[list] = []

        for bt in button:
            options = []
            for j in [0,1]:
                options.append([bt,j])
            if not combinations:
                combinations = [[o] for o in options]
            else:
                combinations = get_combos(options, combinations)



        pressed_count = len(button)
        for c in combinations:
            if check_light(l, c):
                print(f'yay: {l} / {c}')
                # calculate buttons pressed
                pressed_count = min(sum([1 for cc in c if cc[1] == 1]), pressed_count)
        results.append(pressed_count)

    print(f'{sum(results)} --> {results}')


def check_joltage(joltage: list[int], combination:list) -> bool:
    jlen = len(joltage)
    state = [0] * jlen

    for bt in combination:

        if bt[1] == 0:
            continue
        for i in bt[0]:
            state[i] += bt[1]
            if state[i] > joltage[i]:
                return False
        if state == joltage:
            return True
    #print(f'checking {combination}, state: {state} <> {joltage}')
    return False



results = []
for i in range(0, count):
    button = buttons[i]
    jt = joltages[i]

    #max_jt = math.floor(max(jt) / max([max(b) for b in button]))*2
    max_jt = max(jt)

    combinations = None
    for bt in button:
            options = []
            for j in range(0, max_jt):
                options.append([bt,j])
            print(f'got combos')
            if not combinations:
                combinations = [[o] for o in options]
            else:
                combinations = [i for i in get_combos2(options, combinations)]

    print('combinations complete')
    pressed_count = None

    c_counter = 0
    for c in combinations:
        c_counter += 1
        # print(f'checking {c} // {button} // {jt}')
        if check_joltage(jt, c):
            presses = sum([a[1] for a in c])

            if not pressed_count:
                pressed_count = presses
            else:
                pressed_count = min(presses, pressed_count)
            print(f'yay: {jt}, {c} // {presses}')
    results.append(pressed_count)
    print(f'counter: {c_counter} for {jt}')

print(f'{sum(results)} -- {results}')
