from aoc import input


invalid = []
invalid_b = []
for number_range in input()[0].split(','):
    start, end = [int(v) for v in number_range.split('-')]
    for number in range(start, end+1):
        n_str = str(number)

        print(f'{start} - {end} // {number} // {n_str[0]}')


        if n_str[0] == '0':
            invalid.append(number)
            print('invalid! {number}')
        else:
            strlen = len(n_str)
            half = int(strlen/2)

            if strlen % 2 == 0 and n_str[0:half] == n_str[half:]:
                invalid.append(number)
                print(f'invalid! len: {strlen}, {n_str[0:half]} , {n_str[half:]}')
            else:
                for i in range(1, half+1):
                    if strlen % i == 0:
                        parts = []
                        for j in range(0, int(strlen/i)):
                            s = j * i
                            e = s + i
                            parts.append(n_str[s:e])
                            # print(f'adding: {n_str[s:e]} {parts}')

                        if len(set(parts)) == 1:
                            print(f'dups: {i}/{j} {parts}')
                            invalid_b.append(number)


print(invalid)
print(invalid_b)
print(sum(invalid) + sum(invalid_b))
