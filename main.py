import os
import subprocess
import pwd
import sys
import datetime
from collections import deque
from Command import Command
optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-stats','-nofilelist']
optionsWithParameters = ['-before','-after','-match','-bigger','-smaller','-zip']
optionsDict = {'-before':1,'-after':2,'-match':3,'-bigger':4,'-smaller':5,'-delete':6,'-zip':7,'-duplcont':8,'-duplname':9,'-stats':10,'-nofilelist':11}
baseCommand = 'filelist'
exitCommand = 'exit'
commandList = []
resultCommand = ""
baseDir = ""

def main():
	baseDir = getDir()
	getArguments()
	# alttaki iki command lazim olmayabilir onun yerine intersect kullanabiliriz.
	
	#createCommand() 
	#executeCommand(resultCommand)


def getArguments():

	whileFlag = True
	while whileFlag:
		givenCommand = raw_input('Enter command (Type \'exit\' to terminate): ')
		commandTokens = givenCommand.split()
		if commandTokens[0] != baseCommand:
			if commandTokens[0] == exitCommand:
				whileFlag = False
				print 'Terminated'
			else:
				print 'Invalid command given, try again'
				pass
		else:
			# Burasi commandleri isleyecegimiz yer
			if len(commandTokens[1:]) == 0:
				# No option given
				#Directory traverse etcek
				executeCommand('ls')
				#print commandTokens[1:]
			else:
				size = len(commandTokens)
				i = -1 	
				pathlist = []
				while -1*i<size:
					temp = commandTokens[i]
					if isPath(commandTokens,i):
						pathlist.append(commandTokens[i])
					if isOption(commandTokens,i):
						if commandTokens[i] in optionsWithParameters:
							commandList.append(Command(commandTokens[i],pathlist,commandTokens[i+1]))
						else:
							commandList.append(Command(commandTokens[i],pathlist,None))
					i -= 1
					# pathlist = []
				commandList.append(Command('print', '', ''))
				newlist = sorted(commandList, key=lambda x: x.commandType, reverse=False)
				
				for com in newlist:
					#print 'type ',com.commandType
					com.createCommand()
				
		del commandList[:]

def isOption(commandTokens,i):
	if commandTokens[i][0] == '-':
		return True
	else:
		return False

def isPath(commandTokens,i):
	tempStr = baseDir+'/'+commandTokens[i]
	if os.path.isdir(tempStr) or os.path.isdir(commandTokens[i]):
		return True
	else:
		return False
def executeCommand(command):
	os.system(command)
	#output = subprocess.check_output(command,shell=True)
	#print output
def createCommand():
	for com in commandList:
		resultCommand.append(com.createCommand())
		resultCommand.append('&&')
	resultCommand = resultCommand[:-2] # last two && is deleted

def getDir():
	return subprocess.check_output('pwd',shell=True)

if __name__ == '__main__':
	main()