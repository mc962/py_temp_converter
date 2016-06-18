import tkinter
import temperature
#import tkinter.messagebox

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
		#Create frame for unit_from bubble selection
		self.from_list_frame = tkinter.Frame(self.main_window)
		self.from_label = tkinter.Label(self.from_list_frame, text='Convert from:')
		self.from_label.pack(side='top')

# creates radio button lists to allow user to decide which units to convert rom
		self.from_radio = tkinter.IntVar()
		self.fb1 = tkinter.Radiobutton(self.from_list_frame, text= 'Fahrenheit', variable= self.from_radio, value= 1)
		self.fb2 = tkinter.Radiobutton(self.from_list_frame, text= 'Celsius', variable= self.from_radio, value= 2)
		self.fb3 = tkinter.Radiobutton(self.from_list_frame, text= 'Kelvin', variable= self.from_radio, value= 3)
		self.fb1.pack()
		self.fb2.pack()
		self.fb3.pack()
# creates radio button lists to allow user to decide which units to convert rom
		self.to_list_frame = tkinter.Frame(self.main_window)
		self.to_label = tkinter.Label(self.to_list_frame, text='Convert to:')
		self.to_label.pack(side='top')

		self.to_radio = tkinter.IntVar()
		self.tb1 = tkinter.Radiobutton(self.to_list_frame, text= 'Fahrenheit', variable= self.to_radio, value= 1)
		self.tb2 = tkinter.Radiobutton(self.to_list_frame, text= 'Celsius', variable= self.to_radio, value= 2)
		self.tb3 = tkinter.Radiobutton(self.to_list_frame, text= 'Kelvin', variable= self.to_radio, value= 3)
		self.tb1.pack()
		self.tb2.pack()
		self.tb3.pack()
#Create textbox for number input and convert button for actual conversion
		self.convert_frame = tkinter.Frame(self.main_window)
		self.temp_prompt_label = tkinter.Label(self.convert_frame, text='Enter a temperature:')
		self.temp_entry = tkinter.Entry(self.convert_frame, width=10)
		self.temp_prompt_label.pack(side='top')
		self.temp_entry.pack(side='top')
		self.convert_button = tkinter.Button(self.convert_frame, text='Convert')#add a command later
		self.convert_button.pack(side='bottom')
		#Create convert button and tie it to convert function logic area

		#Create instructions button to popup instructions dialog
		##Consider creating reset button
		##Consider creating either error box or dialog

		self.from_list_frame.pack(side='left')
		self.to_list_frame.pack(side='left')
		self.convert_frame.pack(side='right')
		# enter main loop
		tkinter.mainloop()

conv_gui = TempConverterGUI()