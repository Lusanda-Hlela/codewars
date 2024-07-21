def find_multiples(integer, limit):
  result = list()
  for i in range(1, limit + 1):
    m = integer * i
    if m <= limit:
      result.append(m)
  return result