from aoc import input


cables: dict = {}
for line in input(1):
  inp, op = line.split(':')
  cables[inp.strip()] = [o.strip() for o in op.strip().split(' ')]
  


for c in cables:
  print(f'{c} => {cables[c]}')

devices: list = []
nodes = None
outs = 0
while True:  
  if not nodes:
    # start
    nodes = cables['you']
  
  _nodes = []
  for node in nodes:
    print(f'checking: {node}')
    if node not in devices or 1:
      if node == 'out':
        outs += 1
      else:
        devices.append(node)
        print(f'appending: {cables[node]}')
        for n in cables[node]:
          _nodes.append(n)
  nodes = _nodes.copy()
  if len(nodes) == 0:
    break
  
print(f'total outputs: {outs}')
