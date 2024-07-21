def count_sheeps(sheep):
  if len(sheep) > 0:
    for i in sheep:
      if i == True:
        return sheep.count(i)
  else:
    return 0