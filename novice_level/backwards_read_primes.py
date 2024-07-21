def backwards_prime(start, stop):
  base_ten_numbers = list()
  for i in range(start, stop + 1):
    if i > 10:
      base_ten_numbers.append(i)
  
  primes = list()
  for i in base_ten_numbers:
    e = int((i**0.5) + 1)
    if e > 2:
      for j in range(2, e):
        if (i % j) == 0:
          break
      else:
        primes.append(i)

  rprimes = list()
  for i in primes:
    i = str(i)
    i = int(i[::-1])
    f = int((i**0.5) + 1)
    if f > 2:
      for j in range(2, f):
        if ((i % j) == 0) or ((i % 11) == 0):
          break
      else:
        i = str(i)
        k = int(i[::-1])
        i = int(i)
        if i != k:
          rprimes.append(k)
          
  return rprimes