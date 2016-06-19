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
	#print(unit_from, unit_to, temp)
	# unit_from = 'FAHRENHEIT'
	# unit_to = 'CELSIUS'
	# temp = 32
		try:
			if unit_from == 'FAHRENHEIT':
				if unit_to == 'FAHRENHEIT':
					new_temp = temp
				elif unit_to == 'CELSIUS':
					new_temp = (temp - 32)*(5/9.0)
				elif unit_to == 'KELVIN':
					new_temp = (temp + 459.67)*(5/9.0)
				else:
					print('Unknown conversion!')
			######################################
			elif unit_from == 'CELSIUS':
				if unit_to == 'FAHRENHEIT':
					new_temp = (9/5.0)*temp + 32.0
				elif unit_to == 'CELSIUS':
					new_temp = temp
				elif unit_to == 'KELVIN':
					new_temp = temp + 273.15
				else:
					print('Unknown conversion!')
			######################################	
			elif unit_from == 'KELVIN':
				if unit_to == 'FAHRENHEIT':
					new_temp = (9/5.0)*(temp-273.15) + 32
				elif unit_to == 'CELSIUS':
					new_temp = temp - 273.15
				elif unit_to == 'KELVIN':
					new_temp = temp
				else:
					print('Unknown conversion!')
			else:
				'Unknown unit!'
				raise ValueError
		except ValueError:
			print('Invalid unit. Units must be either fahrenheit, celsius, or kelvin.')
		else:
			print('Old temp was: ', temp, 'and new temp is: ', int(round(new_temp, 0)))

main()			