import os
import pwd
import sys
import datetime
import subprocess
from collections import deque

import timestring

optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-stats','-nofilelist']

beforeFiles = []
afterFiles = []
# TODO
# Buradaki createBefore gibi optiona bagli parametreler directory traverse edip match eden file listleri donecek,
# main.py da tum donen file list'lerin intersectini alip bastiracagiz ya da verilen komutu yapacagiz, delete , zip , stats gibi, sadece bu ikisi var sanirim

def file_traverser (qlist):
	file_names = []
	while qlist:
		currentdir = qlist.popleft()
		for files in os.walk(currentdir, topdown=False):
			for file in files[2]:
				file_names.append(files[0] + '/' + file)
	return file_names

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
		# Burasi execute ettigimiz yer burayi sortladiktan sonra teker teker cagiracagiz
		#self.createCommand()

	def getCommandType(self):
		return self.commandType
	def getParameter(self):
		return self.parameter
	def getPathlist(self):
		return self.pathlist

	def createCommand(self):
		if(self.commandType == 1):
			self.createBefore()
		elif(self.commandType == 2):
			self.createAfter()
		elif(self.commandType == 3):
			self.createMatch()
		elif(self.commandType == 4):
			self.createBigger()
		elif(self.commandType == 5):
			self.createSmaller()
		elif(self.commandType == 6):
			self.createDelete()
		elif(self.commandType == 7):
			self.createZip()
		elif(self.commandType == 8):
			self.createDuplcont()
		elif(self.commandType == 9):
			self.createDuplname()
		elif(self.commandType == 10):
			self.createStats()
		elif(self.commandType == 11):
			self.createNofile()

	def createBefore(self):
		param = self.parameter
		date = datetime.datetime.strptime(param,'%Y%m%dT%H%M%S') if len(param) > 9 else datetime.datetime.strptime(param,'%Y%m%d')
		qlist = deque(self.pathlist)
		file_names = file_traverser(qlist)
		print file_names
		for file in file_names:
			modtime = os.path.getmtime(file)
			filetime = datetime.datetime.fromtimestamp(modtime)
			print datetime.datetime.fromtimestamp(modtime).strftime('%Y%m%dT%H%M%S')
			if filetime < date : 
				beforeFiles.append(file)

	def createAfter(self):
		param = self.parameter
		date = datetime.datetime.strptime(param,'%Y%m%dT%H%M%S') if len(param) > 9 else datetime.datetime.strptime(param,'%Y%m%d')
		qlist = deque(self.pathlist)
		file_names = file_traverser(qlist)
		print file_names
		for file in file_names:
			modtime = os.path.getmtime(file)
			filetime = datetime.datetime.fromtimestamp(modtime)
			print datetime.datetime.fromtimestamp(modtime).strftime('%Y%m%dT%H%M%S')
			if filetime > date : 
				afterFiles.append(file)
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