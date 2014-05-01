import Tkinter as tk	   

class OrcusGUI(tk.Frame):			  
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)  
		self.grid()		
		self.getControlInput()
		self.drawMotorStatus()

	
	# Motor control slider callbacks
	def frontLeftMotorValue(self, value = 0):
		print ("FrontLeft: " + str(value))
	def frontRightMotorValue(self, value = 0):
		print ("FrontRight: " + str(value))
	def backLeftMotorValue(self, value = 0):
		print ("BackLeft: " + str(value))
	def backRightMotorValue(self, value = 0):
		print ("BackRight: " + str(value))
	def frontVertMotorValue(self, value = 0):
		print ("FrontVert: " + str(value))
	def BackVertMotorValue(self, value = 0):
		print ("BackVert: " + str(value))
			
	# gets control information from sliders
	def getControlInput(self):
		motorValueCallbacks = [self.frontLeftMotorValue, self.frontRightMotorValue, self.backLeftMotorValue, self.backRightMotorValue, self.frontVertMotorValue, self.BackVertMotorValue]
		
		motorLabels = ["FrontLeft", "FrontRight", "BackLeft", "BackRight", "FrontVert", "BackVert"]
		
		# Create scroll bars for each motor
		for i in range(0,6):
			label = motorLabels[i]
			self.motorScaleLabel = tk.Label(self, text = label)
			self.motorScaleLabel.grid(row = i, column = 1, sticky = tk.W)
			
			self.motorScroll = tk.Scale(self, command=motorValueCallbacks[i], orient=tk.HORIZONTAL)
			self.motorScroll.grid(row = i, column = 2, padx = 0, pady = 10, ipadx = 100)

	# draws ROV motors status
	def drawMotorStatus(self):
		C = tk.Canvas(self, height=275, width=200)
		self.rov = C.create_rectangle(20,20,180,255, fill='#4c0099')
		self.frontLeftMotor = C.create_polygon(30,50,50,50,50,60,30,60, tags='frontLeftMotor')
		C.grid(row = 0, column = 0, rowspan = 6)

gui = OrcusGUI()		
gui.master.geometry("500x500")			   
gui.master.title('ROV ORCUS')  
gui.mainloop()   