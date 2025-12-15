from aoc import input
from math import prod
import re


test = True

data = []
for line in input():
  data.append(line.split())
  
  
h = len(data)
w = len(data[0])

# total = 0
# for i in range(0, w):
#   values = []
#   for j in range(0, h-1):
#     values.append(int(data[j][i]))
#   operator = data[h-1][i]
#     
#   if operator == '*':
#     result = prod(values)
#   else:
#     result = sum(values)
#   
#   total += result
#   print(f'operator: {operator} --> {result} ::  {values} ')
# 
# print(f'total 1: {total}')


data = input()
width = len(data[0])
h = len(data)
print(data)


columns = []
results = []
for i in range(0, width):
    column = []
    _operator = data[h-1][i]
    if _operator != ' ':
      operator = _operator
    end_of_column = False
    for j in range(0, h -1):
      # print(f'getting char at {j}:{i}:{data[j]}')
      char = data[j][i]
      if char == ' ':
        continue
      column.append(char)
    print(f'{i}/{width} --> {column}')
    if len(column) > 0:
      columns.append(int(''.join(column)))
      print(f'b {i}/{width} --> {columns}')

    if len(column) == 0 or i == width -1:
      print(f'performing {operator} on {columns}')
      if operator == '*':
        results.append(prod(columns))
      else:
        results.append(sum(columns))
      columns = []
print(results)
print(sum(results))
