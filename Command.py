import os
import pwd
import sys
import datetime
import subprocess
optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-stats','-nofilelist']

# TODO
# Buradaki createBefore gibi optiona bagli parametreler directory traverse edip match eden file listleri donecek,
# main.py da tum donen file list'lerin intersectini alip bastiracagiz ya da verilen komutu yapacagiz, delete , zip , stats gibi, sadece bu ikisi var sanirim

class Command():
	"""docstring for Command"""
	
	def __init__(self, commandType, pathlist,parameter):
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
		self.pathlist = pathlist
		self.parameter = parameter

	def getCommandType(self):
		return self.commandType
	def getParameter(self):
		return self.parameter
	def getPathlist(self):
		return self.pathlist

	def createCommand(self):
		if(self.commandType == 1):
			createBefore(self)
		elif(self.commandType == 2):
			createAfter(self)
		elif(self.commandType == 3):
			createMatch(self)
		elif(self.commandType == 4):
			createBigger(self)
		elif(self.commandType == 5):
			createSmaller(self)
		elif(self.commandType == 6):
			createDelete(self)
		elif(self.commandType == 7):
			createZip(self)
		elif(self.commandType == 8):
			createDuplcont(self)
		elif(self.commandType == 9):
			createDuplname(self)
		elif(self.commandType == 10):
			createStats(self)
		elif(self.commandType == 11):
			createNofile(self)

	def createBefore(self):
		filepath = getDir()

	def createAfter(self):
		pass
	def createMatch(self):
		pass
	def createBigger(self):
		pass
	def createSmaller(self):
		pass
	def createDelete(self):
		pass
	def createZip(self):
		pass
	def createDuplcont(self):
		pass
	def createDuplname(self):
		pass
	def createStats(self):
		pass
	def createNofile(self):
		pass

def executeCommand(command):
	#os.system(command)
	#output = subprocess.check_output(command,shell=True)
	#print output
	pass
def getDir():
	return subprocess.check_output('pwd',shell=True)