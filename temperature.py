## module for temperature classes

class Temperature():

	def __init__(self, temp):
		self.old_temp = temp


###############################

class Fahrenheit(Temperature):

	def __init__(self, temp, from_unit, to_unit):
		super().__init__(temp)
		self.from_unit = from_unit
		self.to_unit = to_unit
		

	def convert(self):
		if self.to_unit == 'FAHRENHEIT':
			new_temp = self.old_temp
		elif self.to_unit == 'CELSIUS':
			new_temp = (self.old_temp - 32)*(5/9.0)
		elif self.to_unit == 'KELVIN':
			new_temp = (self.old_temp + 459.67)*(5/9.0)
		return new_temp
##############################


class Celsius(Temperature):

	def __init__(self, temp, from_unit, to_unit):
		super().__init__(temp)
		self.from_unit = from_unit
		self.to_unit = to_unit
		

	def convert(self):
		if self.to_unit == 'FAHRENHEIT':
			new_temp = (9/5.0)*self.old_temp + 32.0
		elif self.to_unit == 'CELSIUS':
			new_temp = self.old_temp
		elif self.to_unit == 'KELVIN':
			new_temp = self.old_temp + 273.15
		return new_temp
##############################


class Kelvin(Temperature):

	def __init__(self, temp, from_unit, to_unit):
		super().__init__(temp)
		self.from_unit = from_unit
		self.to_unit = to_unit
		

	def convert(self):
		if self.to_unit == 'FAHRENHEIT':
			new_temp = (9/5.0)*(self.old_temp-273.15) + 32
		elif self.to_unit == 'CELSIUS':
			new_temp = self.old_temp - 273.15
		elif self.to_unit == 'KELVIN':
			new_temp = self.old_temp
		return new_temp
