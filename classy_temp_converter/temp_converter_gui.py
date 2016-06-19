import tkinter
import temperature
import tkinter.messagebox

class TempConverterGUI:
	def __init__(self):
# create main window widget, and set a custom window title
		self.main_window = tkinter.Tk()
		self.main_window.wm_title("Convert Temperatures")

# creates a top frame with label to give a title for the application
		self.top_frame = tkinter.Frame(self.main_window)
		self.title_label = tkinter.Label(self.top_frame, text= 'Temperature Converter')
		self.title_label.pack(side='top')
		self.top_frame.pack()
# create middle frame to hold main program components
		self.mid_frame = tkinter.Frame(self.main_window)
#############################################################################################
#Create frame for unit_from bubble selection
		self.lists_frame = tkinter.Frame(self.mid_frame)
		##########################
		self.from_list_frame = tkinter.Frame(self.lists_frame)
		self.from_label = tkinter.Label(self.from_list_frame, text='Convert from:')
		self.from_label.pack(side='top')

# creates radio button lists to allow user to decide which units to convert from
		self.from_radio = tkinter.StringVar()
		self.fb1 = tkinter.Radiobutton(self.from_list_frame, text= 'Fahrenheit', variable= self.from_radio, value= 'FAHRENHEIT')
		self.fb2 = tkinter.Radiobutton(self.from_list_frame, text= 'Celsius', variable= self.from_radio, value= 'CELSIUS')
		self.fb3 = tkinter.Radiobutton(self.from_list_frame, text= 'Kelvin', variable= self.from_radio, value= 'KELVIN')
		self.fb1.pack()
		self.fb2.pack()
		self.fb3.pack()
		########################
		self.to_list_frame = tkinter.Frame(self.lists_frame)
		self.to_label = tkinter.Label(self.to_list_frame, text='Convert to:')
		self.to_label.pack(side='top')
# creates radio button lists to allow user to decide which units to convert to
		self.to_radio = tkinter.StringVar()
		self.tb1 = tkinter.Radiobutton(self.to_list_frame, text= 'Fahrenheit', variable= self.to_radio, value= 'FAHRENHEIT')
		self.tb2 = tkinter.Radiobutton(self.to_list_frame, text= 'Celsius', variable= self.to_radio, value= 'CELSIUS')
		self.tb3 = tkinter.Radiobutton(self.to_list_frame, text= 'Kelvin', variable= self.to_radio, value= 'KELVIN')
		self.tb1.pack()
		self.tb2.pack()
		self.tb3.pack()
#############################################################################################		
#Create textbox for number input
		self.entry_frame = tkinter.Frame(self.mid_frame)
		

		self.temp_prompt_label = tkinter.Label(self.entry_frame, text='Enter a temperature:')
		self.temp_entry = tkinter.Entry(self.entry_frame, width=10)
		self.temp_prompt_label.pack(side='top')
		self.temp_entry.pack(side='top')
############################################################################################################################################################################
############################################################################################################################################################################		
		#unit_from, unit_to, temp = user_input(self.from_radio, self.to_radio, self.temp_entry)
		
		self.convert_frame = tkinter.Frame(self.mid_frame)

		self.answer = tkinter.StringVar()
		self.answer_label = tkinter.Label(self.convert_frame, textvariable=self.answer)
		self.answer_label.pack(side='bottom')
# convert button for actual conversion
		self.convert_button = tkinter.Button(self.convert_frame, text='Convert', command=self.do_convert)
		self.convert_button.pack(side='top')
#####################################################
		##Consider creating either error box or dialog
# create a bottom frame for miscellaneous buttons
		self.bottom_frame = tkinter.Frame(self.main_window)
		# instructions button that makes dialog box telling how to use app
		self.instructions_button = tkinter.Button(self.bottom_frame, text='Instructions', command=self.instructions)
		self.instructions_button.pack(side='left')
		# quit button that quits app
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		self.quit_button.pack(side='right')
##############################################		
		self.from_list_frame.pack(side='left')
		self.to_list_frame.pack(side='left')

		self.lists_frame.pack(side='left')
		self.convert_frame.pack(side='left')
		self.entry_frame.pack(side='right')
		


		self.mid_frame.pack(side ='top')
		self.bottom_frame.pack(side='bottom')
		# enter main loop
		
		tkinter.mainloop()
		#print(self.from_radio.get(), self.to_radio.get(), self.temp_entry)####look into trying to get variable VALUE from from radio button
	def do_convert(self):
		radio_value = self.from_radio.get()
		if radio_value == 'FAHRENHEIT':
			t_convert = temperature.Fahrenheit(self.temp_entry, self.from_radio, self.to_radio)
			converted_temp = t_convert.convert()
		elif radio_value == 'CELSIUS':
			t_convert = temperature.Celsius(self.temp_entry, self.from_radio, self.to_radio)		
			converted_temp = t_convert.convert()
		elif radio_value == 'KELVIN':
			t_convert = temperature.Kelvin(self.temp_entry, self.from_radio, self.to_radio)
			converted_temp = t_convert.convert()
		
		
		self.answer.set(converted_temp)




	def instructions(self):
		tkinter.messagebox.showinfo('Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
		 'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
		  'Using this information they may convert the entered temperature into the desired unit.')
	# def user_input(self, from_radio_choice, to_radio_choice, temp_entry):
	# 	from_choice = from_radio_choice
	# 	if from_choice == 1:
	# 		from_unit = 'FAHRENHEIT'
	# 	elif from_choice == 2:
	# 		from_unit = 'CELSIUS'
	# 	elif from_choice == 3:
	# 		from_unit = 'KELVIN'

	# 	to_choice = to_radio_choice
	# 	if from_choice == 1:
	# 		to_unit = 'FAHRENHEIT'
	# 	elif from_choice == 2:
	# 		to_unit = 'CELSIUS'
	# 	elif from_choice == 3:
	# 		to_unit = 'KELVIN'

	# 	temperature = float(temp_entry)

	# 	return from_unit, to_unit, temperature
conv_gui = TempConverterGUI()