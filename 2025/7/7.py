from aoc import input, str_replace


splits = 0
data = input()
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


print(f'found part 1: {splits}')


matrix: list[list] = []
for d in data:
  matrix.append(list(d))

for x in range(0, width):
  cell = matrix[1][x]
  if cell == '|':
    matrix[1][x] = 1

for y in range(2, height):
  for x in range(0, width):
    cell = matrix[y][x]
    
    value = 0
    
    if cell == '|':
      # cell directly above
      above = matrix[y-1][x]
      if above != '.':
        value += above 
      
      # check split before 
      if x > 0 and matrix[y][x-1] == '^' and matrix[y-1][x-1] != '.':
        value += matrix[y-1][x-1]

      # check split after
      if x < width -1 and matrix[y][x+1] == '^' and matrix[y-1][x+1] != '.':
        value += matrix[y-1][x+1]

      # overwrite with new value
      matrix[y][x] = value
    
total = sum([d for d in matrix[height-1] if isinstance(d, int)])
print(f'total part 2: {total}')
