def sum_cubes(n):
  result = 0
  for i in range(n + 1):
    if i > 0:
      result += i**3
  return result  