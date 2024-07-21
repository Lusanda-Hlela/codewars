def solution(args):
  l = len(args)
  ranges = list()
  counter = 0

  while l:
    integers = l
    while (integers > 1) and ((args[counter] + 1) == args[counter + 1]):
      ranges.append(args[counter])
      args.pop(counter)
      integers -= 1
    else:
      ranges.append(args[counter])
      if len(ranges) >= 3:
        args.pop(counter)
        args.insert(counter, str(ranges[0]) + '-' + str(ranges[-1]))
        counter += 1
        l -= len(ranges)
        ranges.clear()
      else:
        if len(ranges) == 2:
          args.insert(counter, str(ranges[0]))
          args[counter + 1] = str(ranges[1])
          counter += 2
          ranges.clear()
          l -= 2
        else:
          args[counter] = str(ranges[0])
          counter += 1
          ranges.clear()
          l -= 1

  return ','.join(args)
def solution(args):
  l = len(args)
  ranges = list()
  counter = 0

  while l:
    integers = l
    while (integers > 1) and ((args[counter] + 1) == args[counter + 1]):
      ranges.append(args[counter])
      args.pop(counter)
      integers -= 1
    else:
      ranges.append(args[counter])
      if len(ranges) >= 3:
        args.pop(counter)
        args.insert(counter, str(ranges[0]) + '-' + str(ranges[-1]))
        counter += 1
        l -= len(ranges)
        ranges.clear()
      else:
        if len(ranges) == 2:
          args.insert(counter, str(ranges[0]))
          args[counter + 1] = str(ranges[1])
          counter += 2
          ranges.clear()
          l -= 2
        else:
          args[counter] = str(ranges[0])
          counter += 1
          ranges.clear()
          l -= 1

  return ','.join(args)