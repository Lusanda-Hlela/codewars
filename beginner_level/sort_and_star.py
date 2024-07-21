def two_sort(array):
  arr = array.copy()
  arr.sort()
  r = str()
  for i in arr[0]:
    r += i + '***'
  return r[:-3]