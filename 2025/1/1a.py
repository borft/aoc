from aoc import input
from math import floor

dial = 50
count_zero = 0
count_passing_zero = 0

for line in input(1):

    direction = line[0]
    number = int(line[1:])

    if number > 100:
        count_passing_zero += floor(number /100)
        number = number %100

    if direction == 'L':
        dial -= number
    elif direction == 'R':
        dial += number
    else:
        print(f'ignored: {line}')

    if dial > 99:
        count_passing_zero += floor((dial-1)/100)
        dial = dial %100
    elif dial < 0:
        if dial != -number:
            count_passing_zero += 1
        dial += 100

    if dial == 0:
        count_zero += 1

    print(f'{direction} - {number} - dial:{dial} zc:{count_zero} cpz: {count_passing_zero}')
