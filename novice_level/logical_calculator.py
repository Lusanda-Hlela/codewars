def logical_calc(array, op):
  if len(array) == 1:
    return array[0]
  else:
    while len(array) > 1:
      arr = array[:2]
      if (op == 'AND') and (arr[0] == arr[1]):
        array = [arr[0]] + array[2:]
      elif (op == 'XOR') and (arr[0] != arr[1]):
        array = [True] + array[2:]
      elif (op == 'OR') and ((arr[0] != arr[1]) or ((arr[0] == arr[1]) and (arr[0] == True))):
        array = [True] + array[2:]
      else:
        array = [False] + array[2:]
    else:
      return array[0]