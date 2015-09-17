import Tkinter

class Tk_app(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
		self.entry.grid(column=0,row=0,sticky='EW')
		self.entry.bind("<Return>",self.OnPressEnter)
		
		button = Tkinter.Button(self,text=u'Click me',command=self.OnButtonClick)
		button.grid(column=1,row=0)
		
		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self,fg='blue',bg='red',anchor='w',textvariable=self.labelVariable)
		label.grid(column=0,row=1,columnspan=2,stick='EW')
		
		self.grid_columnconfigure(0,weight=2)
		self.grid_columnconfigure(1,weight=0)
		self.grid_rowconfigure(0,weight=2)
		
		self.resizable(True,False)  #columns,rows
		self.update()
		self.geometry(self.geometry())
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
		
	def OnPressEnter(self,event):
		self.labelVariable.set(self.entryVariable.get())
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
			
	def OnButtonClick(self):
		self.labelVariable.set('You clicked the button!')
		#self.entry.focus_set()
		#self.entry.selection_range(0,Tkinter.END)
		
		
app = Tk_app(None)
app.title('test')
app.mainloop()