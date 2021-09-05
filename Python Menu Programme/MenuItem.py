#1.
class MenuItem:
  #a.
  def __init__ (self, name, category, description, price):
    self.name = name
    self.category = category
    self.description = description
    self.price = price
 
  #b.
  def getName(self):
    return str(self.name)

  def getCategory(self):
    return str(self.category)

  def getDescription(self):
    return str(self.description)

  def getPrice(self):
    return float(self.price)

  def getPriceWithGST(self):
    return float(self.price*1.07)

  def setName(self, name):
    self.name = name
    
  def setCategory(self, category):
    self.category = category

  def setDescription(self, description):
    self.description = description

  def setPrice(self, price):
    self.price = price


