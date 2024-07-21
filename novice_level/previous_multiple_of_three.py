def prev_mult_of_three(n):
  n = str(n)
  while n:
    if (int(n) % 3) != 0:
      if len(n) == 1:
        n = n.split()
        n.clear()
        n = str(n)
        return None
      else:
        n = n[:len(n) - 1]
    else:
      return int(n)