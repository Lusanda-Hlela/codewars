def sumin(n):
  l = list()
  for i in range(1, n * 2, 2):
    while sum(l) < (n ** 2):
      l.append(i)
      break
  l = l[::-1]
  
  f = list()
  while l:
    for i in range(1, n + 1):
      f.append(i * l[0])
      l = l[1:]
  return sum(f)
    
def sumax(n):
  l = list()
  for i in range(1, n * 2, 2):
    while sum(l) < (n ** 2):
      l.append(i)
      break
  
  g = list()
  while l:
    for i in range(1, n + 1):
      g.append(i * l[0])
      l = l[1:]
  return sum(g)
    
def sumsum(n):
  h = sum([i for i in range(1, n + 1)])
  return 2 * n * h