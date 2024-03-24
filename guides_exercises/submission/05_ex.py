# Coding Exercise

# We want to ensure that our size attribute can be retrieved, but not set. Use the appropriate syntax to protect the size attribute. Then, use the 'property' decorator to build a getter to return the protected data. You do not need to instantiate the class.

class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size
    self.cars = []

  # add decorator here
    @property
    def size(self):
      return self._size

  def open_door(self):
    return "The door opens"