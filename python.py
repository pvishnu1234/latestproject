class Computer:

  def __init__(self,a,b):
    self.a = a
    self.b = b
    print(" this init method call initially")
  def new_method(self):
    return self.a+self.b
