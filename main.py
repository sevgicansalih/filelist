import os
import subprocess
import pwd
import sys
import datetime
from collections import deque

def main():
	getArguments()


def getArguments():
	pass

def executeCommand(command):
	os.system(command)
	output = subprocess.check_output(command,shell=True)
	print output

if __name__ == '__main__':
	main()