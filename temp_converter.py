import temperature

def main():

	try:
		unit_from = str(input('Enter units to convert from: '))
		unit_from = unit_from.upper()
		unit_to = str(input('Enter units to convert to: '))
		unit_to = unit_to.upper()

		temp = float(input('Enter temperature: '))
	except ValueError:
		print('Error: Units must be letters and temperature must be a number.')
		print('No blanks allowed')
	else:
		try:
			if unit_from == 'FAHRENHEIT':
				t_convert = temperature.Fahrenheit(temp, unit_from, unit_to)
				converted_temp = t_convert.convert()
			elif unit_from == 'CELSIUS':
				t_convert = temperature.Celsius(temp, unit_from, unit_to)
				converted_temp = t_convert.convert()
			elif unit_from == 'KELVIN':
				t_convert = temperature.Kelvin(temp, unit_from, unit_to)
				converted_temp = t_convert.convert()
			else:
				'Unknown unit!'
				raise ValueError
		except ValueError:
			print('Invalid unit. Units must be either fahrenheit, celsius, or kelvin.')
		else:
			print('Old temp was: ', temp, 'and new temp is: ', converted_temp)
main()