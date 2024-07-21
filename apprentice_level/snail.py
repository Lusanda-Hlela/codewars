def snail(snail_map):
  snake = snail_map
  output = list()
  while len(snake) > 0:
    '''Going right'''
    output.extend(snake[0])
    snake.remove(snake[0])

    if len(snake) > 0:
      '''Going down'''
      for i in snake:
        output.extend([i[-1]])
        del i[-1]

      '''Going left'''
      if snake[-1]:
        output.extend(snake[-1][::-1])
        del snake[-1]

      '''Going up'''
      for i in snake[::-1]:
        output.extend([i[0]])
        del i[0]

  return output