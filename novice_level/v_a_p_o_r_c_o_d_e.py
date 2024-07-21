def vaporcode(s):
  s = s.upper()
  news = str()
  for i in s:
    if i.isspace() == True:
      continue
    news += i + '  '
  return news.rstrip()