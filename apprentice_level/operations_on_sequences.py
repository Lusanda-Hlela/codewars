def solve(arr):
  # Initialize left hand side variables
  a, b, u, v = arr[0], arr[1], arr[2], arr[3]

  # Update input array until the requried non-integer values are obtained
  while arr:
    A = (a * u + b * v)
    B = abs(a * v - b * u)
    arr = arr[4:]
    if len(arr) < 2:
      return [A, B]
    else:
      arr.insert(0, A)
      arr.insert(1, B)
      a, b, u, v = arr[0], arr[1], arr[2], arr[3]