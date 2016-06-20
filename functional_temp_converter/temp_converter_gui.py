import tkinter
import tkinter.messagebox

class TempConverterGUI:
	def __init__(self):
# create main window, and set a custom window title
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
# create frame to hold the unit lists
		self.lists_frame = tkinter.Frame(self.mid_frame)
		##########################
# create frame to hold original unit to convert from list components		
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
# create frame to hold list components to decide which unit to convert to		
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
#Create frame to hold textbox input
		self.entry_frame = tkinter.Frame(self.mid_frame)
		

		self.temp_prompt_label = tkinter.Label(self.entry_frame, text='Enter a temperature:')
		self.temp_entry = tkinter.Entry(self.entry_frame, width=10)


		self.temp_prompt_label.pack(side='top')
		self.temp_entry.pack(side='top')
############################################################################################################################################################################
############################################################################################################################################################################					
# create frame to hold convert button components and answer label components		
		self.convert_frame = tkinter.Frame(self.mid_frame)

# label to display answer
		self.answer = tkinter.StringVar()
		self.answer_label = tkinter.Label(self.convert_frame, textvariable=self.answer)
		self.answer_label.pack(side='bottom')
# convert button for actual conversion
		self.convert_button = tkinter.Button(self.convert_frame, text='Convert', command=self.do_convert)##################################
		self.convert_button.pack(side='top')
#####################################################
		##Consider creating either error box or popup

# create a bottom frame for miscellaneous buttons
		self.bottom_frame = tkinter.Frame(self.main_window)
		# instructions button that makes popup box telling how to use app
		self.instructions_button = tkinter.Button(self.bottom_frame, text='Instructions', command=self.instructions)
		self.instructions_button.pack(side='left')
# quit button that quits app
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		self.quit_button.pack(side='right')
##############################################		
# packup the frames
		self.from_list_frame.pack(side='left')
		self.to_list_frame.pack(side='left')

		self.lists_frame.pack(side='left')
		self.convert_frame.pack(side='left')
		self.entry_frame.pack(side='right')
		


		self.mid_frame.pack(side ='top')
		self.bottom_frame.pack(side='bottom')
		# enter main loop
		
		tkinter.mainloop()
		#print(self.from_radio.get(), self.to_radio.get(), self.temperature)####
	def instructions(self):
		tkinter.messagebox.showinfo('Instructions', 'This application allows the user to convert a temperature between Fahrenheit, Celsius, and Kelvin. '\
		 'A user may select a unit to convert from, a unit to convert to, and what temperature they would like to convert. '\
		  'Using this information they may convert the entered temperature into the desired unit.\n\n'\
		  'Note: Currently answers may be slightly different than expected due to rounding')
#########################################
# called by the convert button, uses from_radio selection to decide who to convert into(which conversion function to call)
	def do_convert(self):
		try:
			self.temperature = float(self.temp_entry.get())
		except ValueError:			
			if self.temp_entry.get() == '':
				value_error_message = 'Temperature may not be blank!'
			else:
				value_error_message = 'Temperature can only be a numerical value!'

			tkinter.messagebox.showinfo('ERROR!', value_error_message)


		else:	
			radio_value = self.from_radio.get()
			if radio_value == 'FAHRENHEIT':
				converted_temp = self.f_convert()
			elif radio_value == 'CELSIUS':
				converted_temp = self.c_convert()
			elif radio_value == 'KELVIN':
				converted_temp = self.k_convert()
	# sets self.answer(and so answer label)	to value returned into converted_temp
			try:
				self.answer.set(converted_temp)
			except UnboundLocalError:
				#print(self.from_radio.get() + '  : ' + self.to_radio.get())
				if self.from_radio.get() == '' and self.to_radio.get() == '':
					tkinter.messagebox.showinfo('ERROR!', 'You must pick units to convert TO and FROM!')
				else:
					tkinter.messagebox.showinfo('ERROR!', 'You must pick units to convert from!')
			# except ValueError:
			# 	tkinter.messagebox.showinfo('ERROR!', 'Temperature may only be a number!')
###########################################################
# series of functions for each individual unit to hold conversion formulas for each possible case
# using self.to_radio selection to decide which conversion to perform, then returns the resulting temperature 
# for use in do_convert	
	def f_convert(self):			
		radio_value = self.to_radio.get()
		try:
			if radio_value == 'FAHRENHEIT':
				new_temp = self.temperature
			elif radio_value == 'CELSIUS':
				new_temp = (self.temperature - 32)*(5/9.0)
			elif radio_value == 'KELVIN':
				new_temp = (self.temperature + 459.67)*(5/9.0)

			return round(new_temp)

		except UnboundLocalError:
			tkinter.messagebox.showinfo('ERROR!', 'You must pick units to convert to!')

	def c_convert(self):		
		radio_value = self.to_radio.get()
		try:
			if radio_value == 'FAHRENHEIT':
				new_temp = (9/5.0)*self.temperature + 32.0
			elif radio_value == 'CELSIUS':
				new_temp = self.temperature
			elif radio_value== 'KELVIN':
				new_temp = self.temperature + 273.15	

			return round(new_temp)

		except UnboundLocalError:
			tkinter.messagebox.showinfo('ERROR!', 'You must pick units to convert to!')
			
	def k_convert(self):		
		radio_value = self.to_radio.get()
		try:
			if radio_value == 'FAHRENHEIT':
				new_temp = (9/5.0)*(self.temperature-273.15) + 32
			elif radio_value == 'CELSIUS':
				new_temp = self.temperature - 273.15
			elif radio_value == 'KELVIN':
				new_temp = self.temperature

			return round(new_temp)
		
		except UnboundLocalError:
			tkinter.messagebox.showinfo('ERROR!', 'You must pick units to convert to!')
			



conv_gui = TempConverterGUI()


# except ValueError:
# 			tkinter.messagebox.showinfo('Error!, A numerical temperature must be entered!')	