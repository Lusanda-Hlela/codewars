from itertools import product

def bishop (start_pos, end_pos, num_moves):
  # List of rows
  r = [i for i in range(1, 9)]

  # Makes cartesian pairs of coordinates
  p = [list(i) for i in product(r, repeat = 2)]

  # Assign letters for a to h numbers for column letters
  c = dict()
  letters = [chr(i) for i in range(ord('a'), ord('h') + 1)]
  counter = 0
  for i in letters:
    c[i] = r[counter]
    counter += 1

  # Translate the start_position from 'LetterNumber' to a cartesian coordinate (x ,y)
  # Find the value of the letter in the start position
  
  sp = [i for i in start_pos]
  a = list()
  for i in c:
    if i == sp[0]:
      a.append(c[i])
      a.append(int(sp[1]))
      
  # Do the same thing for the end_position
  ep = [i for i in end_pos]
  b = list()
  for i in c:
    if i == ep[0]:
      b.append(c[i])
      b.append(int(ep[1]))
  
  # Return all diagonal points of a or the start position
  start_diags = list()
  for i in p:
    if (a != i) and (a[0] != i[0]):
      m = (a[1] - i[1]) / (a[0] - i[0])
      if (m == 1) or (m == -1):
        start_diags.append(i)

  # Return all diagonal points of a or the start position
  end_diags = list()
  for i in p:
    if (b != i) and (b[0] != i[0]):
      m = (b[1] - i[1]) / (b[0] - i[0])
      if (m == 1) or (m == -1):
        end_diags.append(i)

  # Solution Code
  if start_pos == end_pos:
    return True
  elif (start_pos != end_pos) and (num_moves == 0):
    return False
  elif num_moves == 1:
    if (a in end_diags) and (b in start_diags):
      return True
    else:
      return False
  else:
    for i in start_diags:
      for j in end_diags:
        if i != j:
          continue
        else:
          return True
    else:
      return False