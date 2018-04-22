optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-stats','-nofilelist']

class Command():
	"""docstring for Command"""
	
	def __init__(self, commandType, parameters):
		#super(Command, self).__init__()
		if(commandType == optionsList[0]):
			self.commandType = 1
		elif(commandType == optionsList[1]):
			self.commandType = 2
		elif(commandType == optionsList[2]):
			self.commandType = 3	
		elif(commandType == optionsList[3]):
			self.commandType = 4
		elif(commandType == optionsList[4]):
			self.commandType = 5
		elif(commandType == optionsList[5]):
			self.commandType = 6
		elif(commandType == optionsList[6]):
			self.commandType = 7
		elif(commandType == optionsList[7]):
			self.commandType = 8
		elif(commandType == optionsList[8]):
			self.commandType = 9
		elif(commandType == optionsList[9]):
			self.commandType = 10
		elif(commandType == optionsList[10]):
			self.commandType = 11				
		self.parameters = parameters

	def getCommandType(self):
		return self.commandType
	def getParameters(self):
		return self.parameters
	def setCommandType(self,commandType):
		self.commandType = commandType
	def setParameters(self,parameters):
		self.parameters = parameters
