
# Class With Methods

class Circle():
	"""docstring for ClassName"""
	def __init__(self, rarius):
		self.rarius = rarius

	def aera(self):
		return 3.1416 * self.rarius ** 2


class_obj = Circle(5)
cal_aera = round(class_obj.aera())
print("Area is: ", cal_aera)
		