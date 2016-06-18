import unittest
import temperature
import temp_converter

class FahrenheitConvertTestCase(unittest.TestCase):

	def test_f_to_f(self):
		from_unit = 'FAHRENHEIT'
		to_unit = 'FAHRENHEIT'
		temp = 32.0
		t_convert = temperature.Fahrenheit(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, temp)

	def test_f_to_c(self):
		from_unit = 'FAHRENHEIT'
		to_unit = 'CELSIUS'
		temp = 32.0
		t_convert = temperature.Fahrenheit(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 0.0) 

	def test_f_to_k(self):
		from_unit = 'FAHRENHEIT'
		to_unit = 'KELVIN'
		temp = 32.0
		t_convert = temperature.Fahrenheit(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 273.15)


class CelsiusConvertTestCase(unittest.TestCase):

	def test_c_to_c(self):
		from_unit = 'CELSIUS'
		to_unit = 'CELSIUS'
		temp = 0.0
		t_convert = temperature.Celsius(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, temp)

	def test_c_to_f(self):
		from_unit = 'CELSIUS'
		to_unit = 'FAHRENHEIT'
		temp = 0.0
		t_convert = temperature.Celsius(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 32.0)

	def test_c_to_k(self):
		from_unit = 'CELSIUS'
		to_unit = 'KELVIN'
		temp = 0.0
		t_convert = temperature.Celsius(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 273.15)


class KelvinConvertTestCase(unittest.TestCase):

	def test_k_to_k(self):
		from_unit = 'KELVIN'
		to_unit = 'KELVIN'
		temp = 273.15
		t_convert = temperature.Kelvin(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, temp)

	def test_k_to_c(self):
		from_unit = 'KELVIN'
		to_unit = 'CELSIUS'
		temp = 273.15
		t_convert = temperature.Kelvin(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 0.0)

	def test_k_to_f(self):
		from_unit = 'KELVIN'
		to_unit = 'FAHRENHEIT'
		temp = 273.15
		t_convert = temperature.Kelvin(temp, from_unit, to_unit)
		converted_temp = t_convert.convert()
		self.assertEqual(converted_temp, 32.0)


unittest.main()