def sort_the_pile(pile_of_towels, weekly_used_towels):
  while weekly_used_towels:
    if weekly_used_towels[0] == 0:
      weekly_used_towels = weekly_used_towels[1:]
    else:
      pot = pile_of_towels[::-1]
      basket = pot[:weekly_used_towels[0]]
      basket.sort(reverse = True)
      pile_of_towels = pile_of_towels[:-weekly_used_towels[0]]
      pile_of_towels.extend(basket)
      basket.clear()
      weekly_used_towels = weekly_used_towels[1:]
  return pile_of_towels