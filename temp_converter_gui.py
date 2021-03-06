import tkinter
import tkinter.messagebox


class TempConverterGUI:
	"""GUI class to make a tkinter gui for temp_converter application"""
	
	def __init__(self):
		"""__init__ function that starts up the gui, runs main tkinter logic"""
		
		# create main window, and set a custom window title
		self.main_window = tkinter.Tk()
		# set main app_window to desired size and color
		self.main_window.geometry("320x250")
		self.main_window.configure(background = '#ffff66')
		self.main_window.wm_title("Convert Temperatures")

		# creates a top frame with label to give a title for the application
		self.top_frame = tkinter.Frame(self.main_window, background = '#ffff66')
		self.title_label = tkinter.Label(self.top_frame, background = '#ffff66', text= 'Temperature Converter', font=("TkDefaultFont", 20))
		self.title_label.pack(side='top')
		self.top_frame.pack()
		
		# create middle frame to hold main program components
		self.mid_frame = tkinter.Frame(self.main_window, background = '#ffff66')
#############################################################################################
		# create frame to hold the unit lists
		self.lists_frame = tkinter.Frame(self.mid_frame, background = '#ffff66')
		##########################
		# create frame to hold original unit to convert from list components		
		self.from_list_frame = tkinter.Frame(self.lists_frame, background = '#ffff66')
		self.from_label = tkinter.Label(self.from_list_frame, background = '#ffff66', text='Convert from:')
		self.from_label.pack(side='top')

		# creates radio button lists to allow user to decide which units to convert from
		self.from_radio = tkinter.StringVar()
		self.fb1 = tkinter.Radiobutton(self.from_list_frame, background = '#ffff66', text= 'Fahrenheit', width=10, variable= self.from_radio, value= 'FAHRENHEIT')
		self.fb2 = tkinter.Radiobutton(self.from_list_frame, background = '#ffff66', text= 'Celsius', width=10, variable= self.from_radio, value= 'CELSIUS')
		self.fb3 = tkinter.Radiobutton(self.from_list_frame, background = '#ffff66', text= 'Kelvin', width=10, variable= self.from_radio, value= 'KELVIN')
		self.fb1.pack()
		self.fb2.pack()
		self.fb3.pack()
		########################
		# create frame to hold list components to decide which unit to convert to		
		self.to_list_frame = tkinter.Frame(self.lists_frame, background = '#ffff66')
		self.to_label = tkinter.Label(self.to_list_frame, background = '#ffff66', text='Convert to:')
		self.to_label.pack(side='top')
		# creates radio button lists to allow user to decide which units to convert to
		self.to_radio = tkinter.StringVar()
		self.tb1 = tkinter.Radiobutton(self.to_list_frame, background = '#ffff66', text= 'Fahrenheit', width=10, variable= self.to_radio, value= 'FAHRENHEIT')
		self.tb2 = tkinter.Radiobutton(self.to_list_frame, background = '#ffff66', text= 'Celsius', width=10, variable= self.to_radio, value= 'CELSIUS')
		self.tb3 = tkinter.Radiobutton(self.to_list_frame, background = '#ffff66', text= 'Kelvin', width=10, variable= self.to_radio, value= 'KELVIN')
		self.tb1.pack()
		self.tb2.pack()
		self.tb3.pack()
#############################################################################################		
		# create frame to hold textbox input
		self.entry_frame = tkinter.Frame(self.mid_frame, background = '#ffff66')
		

		self.temp_prompt_label = tkinter.Label(self.entry_frame, background = '#ffff66', text='Enter a temperature:')
		self.temp_entry = tkinter.Entry(self.entry_frame, background = '#ffff66', width=10)


		self.temp_prompt_label.pack(side='top')
		self.temp_entry.pack(side='top')

		# give option for rounding, checked to round to integer by default by default
		self.cb_var = tkinter.IntVar()
		self.cb_var.set(1)
		self.cb = tkinter.Checkbutton(self.entry_frame, background = '#ffff66', text='Check to round', variable=self.cb_var)

		self.cb.pack(side='top')
############################################################################################################################################################################
############################################################################################################################################################################					
		# create frame to hold convert button components and answer label components		
		self.convert_frame = tkinter.Frame(self.mid_frame, background = '#ffff66')

		# label to display answer
		self.answer = tkinter.StringVar()
		self.answer_label = tkinter.Label(self.convert_frame, textvariable=self.answer)
		self.answer_label.configure(background='#33ccff', width=10)
		self.answer_label.pack(side='bottom')

		# convert button for actual conversion
		self.convert_button = tkinter.Button(self.convert_frame, text='Convert', command=self.do_convert)##################################
		self.convert_button.pack(side='top')
#####################################################
		# create a bottom frame for miscellaneous buttons
		self.bottom_frame = tkinter.Frame(self.main_window, width=320, height=23, background = '#ffff66')
		# turn off pack_propagate to allow this frame to be sized as desired, allowing buttons to be moved to desired locations in window
		self.bottom_frame.pack_propagate(False)


		# instructions button that makes popup box telling how to use app
		self.instructions_button = tkinter.Button(self.bottom_frame, width=8, text='Instructions', command=self.instructions)
		self.instructions_button.pack(side='left')
		
		# quit button that quits app
		self.quit_button = tkinter.Button(self.bottom_frame, width=8, text='Quit', command=self.main_window.destroy)
		self.quit_button.pack(side='right')
##############################################		
		# packup the frames
		self.from_list_frame.pack(side='left')
		self.to_list_frame.pack(side='left')

		self.entry_frame.pack(side='top')
		self.lists_frame.pack(side='top')
		self.convert_frame.pack(side='top')		

		self.mid_frame.pack(side ='top')		
		self.bottom_frame.pack(side='bottom')
		
		# enter main loop		
		tkinter.mainloop()
	
	
#########################################

	def do_convert(self):
		"""called by the convert button, uses from_radio selection to decide who to convert into(which conversion function to call)"""

		# error counter to keep track of errors, allows us to only popup error box if there are actually any errors		
		error_counter = 0
		
		# while an extra step, allows us to add more error types with minimal revision elsewhere, just += it onto final_error_message	
		# initializes this final_error_message that will go into error message box as blank string	
		final_error_message = ''
				
		try:
			# sets temperature attribute to the value entered into temp_entry (converted into a float)
			self.temperature = float(self.temp_entry.get())
			
			# sets values for the radio_value attributes to the values selected for to and from attributes
			self.from_radio_value = self.from_radio.get()
			self.to_radio_value = self.to_radio.get()

			# decision structure that decides which conversion function to use depending on which radio button value was selected in from list,
			# and then sets the result of those functionns equal to converted temp
			if self.from_radio_value == 'FAHRENHEIT':		
				converted_temp = self.f_convert()
			elif self.from_radio_value == 'CELSIUS':
				converted_temp = self.c_convert()
			elif self.from_radio_value == 'KELVIN':
				converted_temp = self.k_convert()

			# decision structure that rounds the number to either 5 decimals or no decimals depending on how user checked box
			if self.cb_var.get() == 0:
				converted_temp = format(converted_temp, '.5f')
			elif self.cb_var.get() == 1:
				converted_temp = round(converted_temp)
		
			# sets answer(and so answer label)	to value returned into converted_temp
			self.answer.set(converted_temp)

########################################################################################### 
		# UnboundLocalError exception to catch potential ULE errors if user doesn't select 1 or both radio buttons
		except UnboundLocalError:
			# initializes variable that will be added to variable put into final_error_message as blank string
			ule_error_message = ''

			# decides which error message will be used based on which elements are missing
			if self.from_radio.get() == '' and self.to_radio.get() == '':
				ule_error_message = 'You must pick units to convert TO and FROM!\n'								
			elif self.from_radio.get() == '':
				ule_error_message = 'You must pick units to convert FROM!\n'
			elif self.to_radio.get() == '':
				ule_error_message = 'You must pick units to convert TO!\n'

			# adds specific error to final error message
			final_error_message += ule_error_message
			# increments error counter, to be used later for error display
			error_counter+=1


		except ValueError:		
			# initializes variable that will be added to variable put into final_error_message as blank string	
			value_error_message = ''

			# decides which error message will be used based on which elements are missing or incorrect
			if self.temp_entry.get() == '':
				value_error_message = 'Temperature may not be blank!\n'			
			else:
				value_error_message = 'Temperature can only be a numerical value!\n'
			
			# adds specific error to final error message
			final_error_message += value_error_message
			# increments error counter, to be used later for error display
			error_counter+=1

		# displays a messagebox containing the apppropriate error message, but only if there are actually any errors
		if error_counter>0:
			tkinter.messagebox.showinfo('ERROR!', final_error_message)

#####################################################################################################################	
	def f_convert(self):					
		""" 
		f_convert is the part of the series of functions for each individual unit to hold conversion formulas for each possible case
	 	using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
	 	for use in do_convert	
	 	"""

		if self.to_radio_value == 'FAHRENHEIT':
			new_temp = self.temperature
		elif self.to_radio_value == 'CELSIUS':
			new_temp = (self.temperature - 32)*(5/9.0)
		elif self.to_radio_value == 'KELVIN':
			new_temp = (self.temperature + 459.67)*(5/9.0)

		return new_temp
		
	def c_convert(self):				
		""" 
		c_convert is the part of the series of functions for each individual unit to hold conversion formulas for each possible case
	 	using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
	 	for use in do_convert	
	 	"""

		if self.to_radio_value == 'FAHRENHEIT':
			new_temp = (9/5.0)*self.temperature + 32.0
		elif self.to_radio_value == 'CELSIUS':
			new_temp = self.temperature
		elif self.to_radio_value== 'KELVIN':
			new_temp = self.temperature + 273.15	

		return new_temp
		
	def k_convert(self):				
		""" 
		k_convert is the part of the series of functions for each individual unit to hold conversion formulas for each possible case
	 	using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
	 	for use in do_convert	
	 	"""			

		if self.to_radio_value == 'FAHRENHEIT':
			new_temp = (9/5.0)*(self.temperature-273.15) + 32
		elif self.to_radio_value == 'CELSIUS':
			new_temp = self.temperature - 273.15
		elif self.to_radio_value == 'KELVIN':
			new_temp = self.temperature

		return new_temp
		
	def instructions(self):
		""" instructions is called by the instructions button, makes a popup window to show user how to use app """
		tkinter.messagebox.showinfo('Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
		 'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
		  'Using this information they may convert the entered temperature into the desired unit.\n\n'\
		  'Note: Currently answers may be slightly different than expected due to rounding\n'\
		  'User may uncheck box for rounding to get number up until 4 decimal points, which should allow users to account for potential fringe cases with erroneous division.')

# creates an instance of TempConverterGUI to run the program
conv_gui = TempConverterGUI()
