def howmuch(m, n):
  if m > n:
    largest = m
    smallest = n
  elif m < n:
    largest = n
    smallest = m
  else:
    largest = n
    smallest = n

  result = list()
  for i in range(smallest, largest + 1):
    b = (i - 2) / 7
    c = (i - 1) / 9
    if (int(b) == b) and (int(c) == c):
      r = [f"M: {int(i)}", f"B: {int(b)}", f"C: {int(c)}"]
      result.append(r)
  return result