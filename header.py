import os
import subprocess
import time

# -----------------classes----------------- #
class colors:
	reset = '\033[0m'
	bold = '\033[01m'
	disable = '\033[02m'
	underline = '\033[04m'
	reverse = '\033[07m'
	strikethrough = '\033[09m'
	invisible = '\033[08m'
 
	class fg:
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		orange = '\033[33m'
		blue = '\033[34m'
		purple = '\033[35m'
		cyan = '\033[36m'
		lightgrey = '\033[37m'
		darkgrey = '\033[90m'
		lightred = '\033[91m'
		lightgreen = '\033[92m'
		yellow = '\033[93m'
		lightblue = '\033[94m'
		pink = '\033[95m'
		lightcyan = '\033[96m'

	class bg:
		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		orange = '\033[43m'
		blue = '\033[44m'
		purple = '\033[45m'
		cyan = '\033[46m'
		lightgrey = '\033[47m'
# ----------------------------------------- #

# ----------------------------------------- #
print( f"\n\n{ colors.fg.cyan }\t /$$                              /$$                   /$$$$$$ /$$                        /$$      { colors.reset }" )     
print( f"{ colors.fg.cyan }\t| $$                             | $$                  /$$__  $| $$                       | $$      { colors.reset }" )
print( f"{ colors.fg.cyan }\t| $$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$ /$$$$$$  /$$$$$$| $$  \__| $$$$$$$  /$$$$$$  /$$$$$$| $$   /$${ colors.reset }" )
print( f"{ colors.fg.cyan }\t| $$__  $$/$$__  $$|____  $$/$$__  $$/$$__  $$/$$__  $| $$     | $$__  $$/$$__  $$/$$_____| $$  /$$/{ colors.reset }" )
print( f"{ colors.fg.cyan }\t| $$  \ $| $$$$$$$$ /$$$$$$| $$  | $| $$$$$$$| $$  \__| $$     | $$  \ $| $$$$$$$| $$     | $$$$$$/ { colors.reset }" )
print( f"{ colors.fg.cyan }\t| $$  | $| $$_____//$$__  $| $$  | $| $$_____| $$     | $$    $| $$  | $| $$_____| $$     | $$_  $$ { colors.reset }" )
print( f"{ colors.fg.cyan }\t| $$  | $|  $$$$$$|  $$$$$$|  $$$$$$|  $$$$$$| $$     |  $$$$$$| $$  | $|  $$$$$$|  $$$$$$| $$ \  $${ colors.reset }" )
print( f"{ colors.fg.cyan }\t|__/  |__/\_______/\_______/\_______/\_______|__/      \______/|__/  |__/\_______/\_______|__/  \__/{ colors.reset }" )
print( f"\n                                                     By: { colors.bold + colors.fg.yellow } DEL-YAAG { colors.reset }[driely]" )
# ----------------------------------------- #

# ----------------functions---------------- #
# loaing func
def loading( number ):
	for i in range( number ):
		print(f"{ colors.bg.purple + colors.fg.black }#{ colors.reset }", end="", flush=True)
		time.sleep(0.05)
	print("")

# split the path and return new one from the working directory
def filePathFromWD( filePath, directory ):
	find = filePath.find( directory )
	newPath = filePath[ find + 1 + len(directory): ].strip()
	return newPath

# check login in file
def openFileAndCheckLogin( filePath, newPath, fileName ):
	with open( filePath, 'r', encoding='utf-8', errors='ignore' ) as file:
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
					print( f'{ colors.fg.green + newPath } OK { colors.reset }' )
				else:
					print( f'{ colors.fg.red + newPath } KO { colors.reset }' )
		if not isHeader:
			print( f"{ colors.fg.yellow + newPath }missing header in { fileName }! { colors.reset }" )

# walk in the workin directory and its subdirectories and open all files and check them
def checkFilesForAutor( directory ):
	totalFiles = 0
	for root, dirs, files in os.walk( directory ):
		for fileName in files:
			if fileName.endswith( ( ".cpp", ".hpp", ".c", ".h" ) ):
				filePath = os.path.join( root, fileName )
				newPath = filePathFromWD( filePath, directory )
				totalFiles += 1
				openFileAndCheckLogin( filePath, newPath, fileName )
	if totalFiles > 0:
		print( f'______________________________' )
		for loginName, occurences in loginOccurences.items():
			percentage = ( ( occurences / totalFiles ) * 100 ) / 3
			formattedPercentage = "{:.2f}".format( percentage )
			print( f'{ colors.fg.yellow + formattedPercentage }%\t\t{ loginName + colors.reset }' )
# ----------------------------------------- #

# ------------------start------------------ #
# get the intput
inputLogin = input( f"{ colors.bold + colors.fg.orange }Enter login:{ colors.reset } " )
if not len( inputLogin ) or inputLogin.isspace():
	exit( 0 )


# check norminette
print( f'\n{ colors.bg.green + colors.fg.black }  -- Check Norminette --  { colors.reset }' )
loading( 26 )
result = subprocess.run( [ "norminette" ], shell=True )

# split the logins and store them in dictionary
login = inputLogin.split( ' ' )
login = [ part.strip() for part in login if part.strip() ]
loginOccurences = { loginName: 0 for loginName in login }

# check haders in all files
print( f'\n{ colors.bg.green + colors.fg.black }    -- Check Header --    { colors.reset }')
loading( 26 )
currentDirectory = os.getcwd()
checkFilesForAutor( currentDirectory )
print( f'______________________________' )

# status of norminette { OK, KO }
if result.returncode == 0:
	print( f'{ colors.fg.green }Norminette\tOK { colors.reset }' )
else:
	print( f'{ colors.fg.red }Norminette\tKO{ colors.reset }' )
print( f'______________________________' )
# ----------------------------------------- #