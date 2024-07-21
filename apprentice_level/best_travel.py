from itertools import combinations

def choose_best_sum(t, k, ls):
  # Generate a list of distance combinations of length k
  towns = list(combinations(ls, k))
  best_travel = list()
  for i in towns:
    i = sum(i)
    if i <= t:
      best_travel.append(i)
    else:
      continue
  
  if len(best_travel) > 0:
    return max(best_travel)
  else:
    return None