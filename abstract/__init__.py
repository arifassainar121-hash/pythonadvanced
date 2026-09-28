from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(shape):

  def __init__(self, width, height):
    self.width =int(input('ener the width: '))
    self.height =int(input('enter the height: '))

  def get_area(self):
    print('area',self.width * self.height)

  def get_perimeter(self):
    print('perimeter',self.width + self.height)



r=Rectangle()
r.get_area()
r.get_perimeter()