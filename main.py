import os
import subprocess
import pwd
import sys
import datetime
from collections import deque
from Command import Command
optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-stats','-nofilelist']
optionsDict = {'-before':1,'-after':2,'-match':3,'-bigger':4,'-smaller':5,'-delete':6,'-zip':7,'-duplcont':8,'-duplname':9,'-stats':10,'-nofilelist':11}
baseCommand = 'filelist'
exitCommand = 'exit'

def main():
	getArguments()


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
				# Check for options and parameters
				command1 = Command('-before','par1')
				print command1.getCommandType(),' ',command1.getParameters()
def executeCommand(command):
	os.system(command)
	#output = subprocess.check_output(command,shell=True)
	#print output

if __name__ == '__main__':
	main()