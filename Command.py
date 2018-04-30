import os
import pwd
import sys
import datetime
import subprocess
import re
import zipfile
from collections import deque

optionsList = ['-before','-after','-match','-bigger','-smaller','-delete','-zip','-duplcont','-duplname','-nofilelist','-stats', 'print']

current_files = []
global_files = []
duplcont_list = []
duplname_list = []
stats_check = False
nofile_check = False
duplcont_check = False
duplname_check = False

"""
total number of files visited, total size of files visited, total number of files listed, total size of files listed, 
total number of unique files listed, total size of unique files,
total number of files with unique names
"""
stats = [0, 0, 0, 0, 0, 0, 0] 
stats_text = ['Total number of files visited: ', 'Total size of files visited: ', 'Total number of files listed: ', 'Total size of files listed: ',
 'Total number of unique files listed: ', 'Total size of unique files: ', 'Total number of files with unique names: ']

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

	if stats[0] == 0:
		update_stats(file_names, 0)
	return file_names

def update_stats(file_names, format): #format:0 total format:1 listed format:2 duplcont format:3 duplname
	if format == 0:
		stats[0] = len(file_names)
		for file in file_names:
			st = os.stat(file)
			filesize = st.st_size
			stats[1] = stats[1] + filesize
	elif format == 1:
		if not nofile_check:
			stats[2] = len(file_names)
			for file in file_names:
				st = os.stat(file)
				filesize = st.st_size
				stats[3] = stats[3] + filesize
		else:
			stats[2] = 0
			stats[3] = 0
	elif format == 2:
		cnt = 0
		size = 0
		for dupl in file_names:
			st = os.stat(dupl[0])
			filesizes = st.st_size * len(dupl)
			cnt = cnt + len(dupl)
			size = size + filesizes
		stats[4] = stats[0] - cnt
		stats[5] = stats[1] - size
	elif format == 3:
		cnt = 0
		for dupl in file_names:
			cnt = cnt + len(dupl)
		stats[6] = stats[0] - cnt

def printer():
	if nofile_check == False:
		print '------\nFILES\n------'
		for file in global_files:
			print file
		if duplcont_check:
			print '------\nduplcont files\n------'
			for dupl in duplcont_list:
				for file in dupl:
					print file
				print '------'
		if duplname_check:
			print '------\nduplname files\n------'
			for dupl in duplname_list:
				for file in dupl:
					print file
				print '------'
	if stats_check == True:
		print '\n------\nSTATS\n------'
		print stats_text[0] + str(stats[0])
		print stats_text[1] + str(stats[1])
		print stats_text[2] + str(stats[2])
		print stats_text[3] + str(stats[3])
		if duplcont_check == True:
			print stats_text[4] + str(stats[4])
			print stats_text[5] + str(stats[5])
		if duplname_check == True:
			print stats_text[6] + str(stats[6])

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

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
		elif(commandType == optionsList[11]):
			self.commandType = 12				
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
			self.createNofile()
		elif(self.commandType == 11):
			self.createStats()
		elif(self.commandType == 12):
			self.printResult()

	def createBefore(self):
		global global_files
		global current_files
		param = self.parameter
		date = datetime.datetime.strptime(param,'%Y%m%dT%H%M%S') if len(param) > 9 else datetime.datetime.strptime(param,'%Y%m%d')
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		for file in file_names:
			modtime = os.path.getmtime(file)
			filetime = datetime.datetime.fromtimestamp(modtime)
			if filetime < date : 
				current_files.append(file)
		global_files = current_files[:] if len(global_files) == 0 else intersection(global_files, current_files)
		current_files = []

	def createAfter(self):
		global global_files
		global current_files
		param = self.parameter
		date = datetime.datetime.strptime(param,'%Y%m%dT%H%M%S') if len(param) > 9 else datetime.datetime.strptime(param,'%Y%m%d')
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		for file in file_names:
			modtime = os.path.getmtime(file)
			filetime = datetime.datetime.fromtimestamp(modtime)
			if filetime > date : 
				current_files.append(file)
		global_files = current_files[:] if len(global_files) == 0 else intersection(global_files, current_files)
		current_files = []

	def createMatch(self):
		global global_files
		global current_files
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		pattern = self.parameter
		prog = re.compile(pattern,re.DOTALL)
		for file in file_names:
			index = file.rfind('/')
			filename = file[index+1:] if index != 1 else file
			result = bool(prog.search(file))
			if result:
				current_files.append(file)
		global_files = current_files[:] if len(global_files) == 0 else intersection(global_files, current_files)
		current_files = []

	def createBigger(self):
		global global_files
		global current_files
		param = self.parameter
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		for file in file_names:
			st = os.stat(file)
			filesize = st.st_size
			if filesize >= int(param) : 
				current_files.append(file)
		global_files = current_files[:] if len(global_files) == 0 else intersection(global_files, current_files)
		current_files = []

	def createSmaller(self):
		global global_files
		global current_files
		param = self.parameter
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		for file in file_names:
			st = os.stat(file)
			filesize = st.st_size
			if filesize <= int(param) : 
				current_files.append(file)
		global_files = current_files[:] if len(global_files) == 0 else intersection(global_files, current_files)
		current_files = []

	def createDelete(self):
		global global_files
		global current_files
		param = self.parameter
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)

		for file in file_names:
			os.remove(file)

	def createZip(self):
		global global_files
		global current_files
		param = self.parameter
		zipf = zipfile.ZipFile(param, 'w', zipfile.ZIP_DEFLATED)

		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)

		for file in file_names:
			zipf.write(file)

		zipf.close()

	def createDuplcont(self):
		global global_files
		global duplcont_list
		global duplcont_check
		dictDuplcont = {}
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)

		for file in file_names:
			with open(file, 'r') as content_file:
				content = content_file.read()
				dictDuplcont[file] = content
		rev_multidict = {}
		for key, value in dictDuplcont.items():
			rev_multidict.setdefault(value, set()).add(key)
		
		for cur_set in [values for key, values in rev_multidict.items() if len(values) > 1]:
			cur_list = list(cur_set)
			duplcont_list.append(cur_list)
		update_stats(duplcont_list, 2)
		duplcont_check = True

	def createDuplname(self):
		global global_files
		global duplname_list
		global duplname_check
		dictDuplname = {}
		qlist = deque(self.pathlist)
		file_names = global_files[:] if len(global_files) > 0 else file_traverser(qlist)
		
		for file_path in file_names:
			index = file_path.rfind('/')
			filename = file_path[index+1:] if index != 1 else file_path
			dictDuplname[file_path] = filename

		rev_multidict = {}
		for key, value in dictDuplname.items():
			rev_multidict.setdefault(value, set()).add(key)
		
		for cur_set in [values for key, values in rev_multidict.items() if len(values) > 1]:
			cur_list = list(cur_set)
			duplname_list.append(cur_list)
		update_stats(duplname_list, 3)
		duplname_check = True

	def createStats(self):
		global global_files
		global stats_check
		stats_check = True
		update_stats(global_files, 1)

	def createNofile(self):
		global nofile_check
		nofile_check = True
	
	def printResult(self):
		printer()

def executeCommand(command):
	#os.system(command)
	#output = subprocess.check_output(command,shell=True)
	#print output
	pass
def getDir():
	return subprocess.check_output('pwd',shell=True)