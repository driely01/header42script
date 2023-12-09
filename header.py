import os

RESET   = "\033[0m"
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
BLUE	= "\033[94m"

currentDirectory = os.getcwd()
inputLogin = input( "Enter login: " )
if not len(inputLogin):
	exit(0)
login = inputLogin.split(' ')
login = [ part.strip() for part in login if part.strip() ]
loginOccurences = { loginName: 0 for loginName in login }

def openFileAndCheckLogin( filePath, fileName ):
	with open(filePath, 'r', encoding='utf-8', errors='ignore') as file:
		lines = file.readlines()
		isHeader = False
		for line in lines:
			if "#include" in line:
				break
			if "By: " in line or "Created: " in line or "Updated: " in line:
				isHeader = True
				flag = False
				for loginName in login:
					if loginName in line:
						loginOccurences[loginName] += 1
						flag = True
						break
				if flag:
					print(f'{GREEN + loginName + " " + fileName} Ok { RESET }')
				else:
					print(f'{RED + fileName} cheater { RESET }')
		if not isHeader:
			print(f"{ BLUE }missing header in { fileName }! { RESET }")



def checkFilesForAutor(directory):
	totalFiles = 0
	for root, dirs, files in os.walk(directory):
		for fileName in files:
			if fileName.endswith((".cpp", ".hpp", ".c", ".h")):
				filePath = os.path.join(root, fileName)
				totalFiles += 1
				openFileAndCheckLogin( filePath, fileName )
	if totalFiles > 0:
		print(f'____________________')
		for loginName, occurences in loginOccurences.items():
			percentage = ( ( occurences / totalFiles ) * 100 ) / 3
			formattedPercentage = "{:.2f}".format( percentage)
			print(f'{ BLUE + formattedPercentage }%	{ loginName + RESET }')
				
checkFilesForAutor(currentDirectory)
