class Car:
	"""docstring for Car"""
	def __init__(self, model, color):
		self.model = model
		self.color = color

	def display_info(self):
		print(f"Model: {self.model} & Color: {self.color}.")


car_obj = Car("HONDA", "Black")
car_obj.display_info()		