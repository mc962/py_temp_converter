# imports temperature module to use individual temperature classes and their conversions
import temperature

def main():
# try block to catch incorrect input of units
	try:
# sets appropriate unit_from, to, and temp values to values returned from user_input function		
		unit_from, unit_to, temp = user_input()
# ValueError exception that is raised if strings are not inputted for units and numbers are not inputted for temp				
	except ValueError:
		print('Error: Units must be letters and temperature must be a number.')
		print('No blanks allowed')
# if legal units and temps were entered, then proceeds with application		
	else:
# try block to catch if unknown unit was entered (e.g. mispelled temperature unit, etc.)		
		try:
# decision structure that, depending on what is converted from, creates a new temperature object of that type, passing the inputted values
# convert function is then performed on that object (which selects for appropriate conversion based on unit_to value), and then
# returns that value to converted_temp to be used later
			if unit_from == 'FAHRENHEIT':
				t_convert = temperature.Fahrenheit(temp, unit_from, unit_to)
				
			elif unit_from == 'CELSIUS':
				t_convert = temperature.Celsius(temp, unit_from, unit_to)
				
			elif unit_from == 'KELVIN':
				t_convert = temperature.Kelvin(temp, unit_from, unit_to)
			
# in the case of an unknown unit (e.g. mispelled units, etc.), then a value error is manually raised
			else:
				'Unknown unit!'
				raise ValueError
# valuerror that is raised when invalid temp units were given				
		except ValueError:
			print('Invalid unit. Units must be either fahrenheit, celsius, or kelvin.')
# if no value errors were raised, then finishes application with appropriate output		
		else:
			converted_temp = t_convert.convert()
			print('Old temp was: ', temp, 'and new temp is: ', converted_temp)

# function to get user input
def user_input():
# gets user input for from, to units and temp, capitalizes the units (for ease of use)
	unit_from = str(input('Enter units to convert from: '))
	unit_from = unit_from.upper()
	unit_to = str(input('Enter units to convert to: '))
	unit_to = unit_to.upper()

	temp = float(input('Enter temperature: '))
# returns the gathered data for further application use
	return unit_from, unit_to, temp

if __name__ == '__main__':
    main()