from aoc import input
from math import sqrt, prod

boxes = []
for line in input():
  boxes.append([int(v.strip()) for v in line.split(',')])

def get_distance(b1: [int], b2: [int]) -> float:
  return sqrt( 
    (b1[0]-b2[0])**2
    +(b1[1]-b2[1])**2
    +(b1[2]-b2[2])**2
    )
    


def flatten_box(box: list[int]) -> str:
  return '_'.join([str(b) for b in box])

index = {}
distances = {}
box_count = len(boxes)
for b1_index in range(0, box_count):
  b1 = boxes[b1_index]
  index[flatten_box(b1)] = b1_index
  
  for b2_index in range(b1_index+1, box_count):
    b2 = boxes[b2_index]
    key = (flatten_box(b1), flatten_box(b2))
    d = get_distance(b1, b2)
    distances[key] = d 

sorted_keys = dict(sorted(distances.items(), key=lambda item: item[1]))


a = 0
for s in sorted_keys:
  print(s)
  a+=1
  if a ==20:
    break

def check_overlap(cs: list):

  result = []
  for c in cs:
    no_add = True
    for key, r in enumerate(result):
      for b1 in c:
        if b1 in r:
          # found dupe
          #print(f'found dupe: {b1} {result} {cs}')
          t = list(set(r+c))
          result[key] = t
          no_add = False
          break
      if not no_add:
        break
    if no_add:
      result.append(c)
  
  total = 0
  for r in result:
    total += len(r)
#   if total != 1000:
#     print(f'WRONG!! --> {total}')
#     print(result)
#     exit(1)
#   
  return result


# 10 max
circuits = [[c] for c in list(index.keys())]

ledger = []

i = 0
for b in sorted_keys:
  #b = sorted_keys[i]
  print(f'{b} --> {distances[b]}')
  for c in circuits:
    if b[0] in c or b[1] in c:
      if b[0] not in c:
        c.append(b[0])
        ledger.append(b[0])
      if b[1] not in c:
        c.append(b[1])
        ledger.append(b[1])
      circuits = check_overlap(circuits)

  i += 1
  #if i == 1001:
  if len(circuits) == 1:
    break

#print(sorted_keys)


# 1716 too low
# 352584 right
print(f'total: {sum([len(c) for c in circuits])}')
top3 = sorted([len(c) for c in circuits], reverse=True)[:3]

print(f'top: {top3} // {prod(top3)}')

xs = [int(l.split('_')[0]) for l in ledger[-2:]]
print(prod(xs))

# for c in circuits:
#   print(len(c))
