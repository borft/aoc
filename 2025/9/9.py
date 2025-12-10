from aoc import input


tiles = []
for line in input():
    tiles.append([int(i) for i in line.split(',')])
    
max_area = 0
tc = len(tiles)

for i in range(0, tc):
  for j in range(i+1, tc):
    
    # calculate area
    w = abs(tiles[i][0] - tiles[j][0]) + 1
    h = abs(tiles[i][1] - tiles[j][1]) + 1
    area = w*h
    
    if area > max_area:
      max_area = area
      
      
      
print(f'found: {max_area}')
