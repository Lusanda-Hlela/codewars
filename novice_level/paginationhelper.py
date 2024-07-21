# TODO: complete this class

class PaginationHelper:

  # The constructor takes in an array of items and an integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.col = collection
    self.ipp = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.col)
  
  # returns the number of pages
  def page_count(self):
    '''nop: number of pages'''
    nop = len(self.col) / self.ipp   # int rounds everything down
    if nop > int(nop):
      nop = int(nop + 1)
    else:
      nop = int(nop)
    return nop

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self, page_index):
    '''Find the maximum page index value'''
    nop = len(self.col) / self.ipp 
    if nop > int(nop):
      nop = int(nop + 1)
    else:
      nop = (int(nop))
    
    '''iv: index value'''
    iv = list()
    for i in range(nop):
      iv.append(i)
    
    '''Find the number of items on the last page'''
    '''a: number of pages with full items'''
    a = len(self.col) // self.ipp
    
    '''b: total number of items in full pages'''
    b = a * self.ipp

    '''c: number of items on the last page'''
    c = len(self.col) - b
    
    '''Create a list that assigns number of items per page'''
    pi = list()
    '''When the last page does not have the total items per page'''
    if a < nop:
      while len(pi) < (nop - 1):
        pi.append(self.ipp)
    pi.append(c)
    
    '''When the last page has the total items per page'''
    if a == nop:
      while len(pi) < nop:
        pi.append(self.ipp)
    
    '''Access the list and return the number of items in that page'''
    try:
      if (pi[page_index] in pi) and (page_index >= 0 and page_index < nop):
        return pi[page_index]
    except IndexError:
      return -1

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self, item_index):
    coll = list()
    for i in self.col:
      coll.append(i)
    
    p = list()    
    while coll:
      p.append(coll[:self.ipp])
      coll = coll[self.ipp:]

    ind = -1
    if item_index >= 0:
      try:
        for j in p:
          for k in j:
            if (self.col[item_index] in self.col) and (k == self.col[item_index]):
              ind = p.index(j)
      except IndexError:
        ind = ind
    elif len(self.col) == 0:
      ind = ind
    return ind