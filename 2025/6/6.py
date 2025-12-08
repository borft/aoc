from aoc import input
from math import prod


data = []
for line in input():
  data.append(line.split())
  
  
h = len(data)
w = len(data[0])

total = 0

for i in range(0, w):
  values = []
  for j in range(0, h-1):
    values.append(int(data[j][i]))
  operator = data[h-1][i]
  
  if operator == '*':
    result = prod(values)
  else:
    result = sum(values)
  
  total += result
  print(f'operator: {operator} --> {result} ::  {values} ')

print(f'total: {total}')
