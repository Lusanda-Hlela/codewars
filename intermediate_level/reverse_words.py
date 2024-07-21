def reverse_words(text):
  '''Make a copy the input string'''
  rtext = text
  '''Return the position of whitespaces from the input string'''
  spaces = list()
  for word in rtext:
    if (word.isspace()) == True:
      '''Return the index of the last whitespace'''
      x = rtext.rfind(word)
      '''Collect the index of the last whitespace'''
      spaces.append(x)
      '''Remove the last whitespace from the string'''
      rtext = rtext[:x]
  '''Reverse the order of whitespace positions'''
  spaces.reverse()

  '''Reverse the input string'''
  text = text[::-1]
  '''Convert the reversed string into a list of word items'''
  text = text.split()
  '''Reverse the order of reversed words'''
  text.reverse()
  '''Convert the reversed list of words into a string'''
  text = ''.join(text)  

  '''Add spaces on the reversed text''' 

  answer = str()

  for i in text:
    answer += i
    for j in spaces:
      if len(answer) == j:
        answer += ' '
  
  return answer