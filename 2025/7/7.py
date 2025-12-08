from aoc import input, str_replace


splits = 0
data = input(1)
height = len(data)
width = len(data[0])

for h in range(0, height):
  line = data[h]
  for w in range(0, width):
    c = line[w]
    if c == '.':
      if data[h-1][w] == '|':
        data[h] = str_replace(data[h], w, '|')
    elif c == 'S':
      print(f'found start at {h}:{w}')
      data[h+1] = str_replace(data[h+1], w, '|')
    elif c == '|' and data[h+1][w] == '.':
      # if we find a pipe, a period below if becomes a pipe also
      data[h+1] = str_replace(data[h+1], w, '|')
    elif c == '^' and h > 0:
      if data[h-1][w] == '|':
        # a pipe hits ^, we split
        splits += 1
        data[h] = str_replace(data[h], w-1, '|')
        data[h] = str_replace(data[h], w+1, '|')


print(f'found: {splits}')


for d in data:
  print(d)
