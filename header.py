import os

RESET   = "\033[0m"
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"

inputlogin = input( "Enter login: " )
if not inputlogin:
	exit(0)
login = inputlogin.split(' ')

def openFileAndCheckLogin( file_path, file_name ):
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
		lines = file.readlines()
		for line in lines:
			if "#include" in line:
				break
			if "By: " in line or "Created: " in line or "Updated: " in line:
				flag = False
				for loginName in login:
					if loginName in line:
						flag = True
						break
				if flag:
					print(f'{GREEN + loginName + " " + file_name} Ok { RESET }')
				else:
					print(f'{RED + file_name} cheater { RESET }')

def check_files_for_author(directory):
	for root, dirs, files in os.walk(directory):
		for file_name in files:
			if file_name.endswith(".cpp"):
				file_path = os.path.join(root, file_name)
				openFileAndCheckLogin( file_path, file_name )
				
current_directory = os.getcwd()
check_files_for_author(current_directory)