'''
+------------------+
| AutoFileArranger |
+------------------+
by Bishal jaiswal Copyright (c) 2022
'''

import os
from time import sleep

clutterCount = 0

def createIfNotExist(folder):
	if not os.path.exists(folder):
		os.mkdir(folder)

def moveFile(files:str,folderName:str) ->None:
	for file in files:
		sleep(2)
		print(f"[*] Moving {file} To {folderName} Folder")
		os.replace(file,f"{folderName}/{file}")
		sleep(2)

	if not len(os.listdir(folderName)) >clutterCount:
		print(f"[i] {len(os.listdir(folderName))} Files is in {folderName} Folder\n")
	else:
		print("[!] No files to be moved")
	

files = os.listdir()
files.remove("mian.py")

imgExt = ['.png','.jpg','.bmp']
docExt = ['.docx','.doc','xml','.txt','.rtf']
musicExt = ['.mp3','.mp4','mp5']

imageFiles = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
clutterCount+=len(imageFiles)

documentFiles = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
clutterCount+=len(documentFiles)

musicFiles = [file for file in files if os.path.splitext(file)[1].lower() in musicExt]
clutterCount+=len(musicFiles)

otherFiles = []
for file in files:
	if os.path.splitext(file)[1] not in imgExt and os.path.splitext(file)[1] not in docExt and os.path.splitext(file)[1] not in musicExt and os.path.isfile(file):
		otherFiles.append(file)

clutterCount+=len(otherFiles)

	
if __name__ == "__main__":	
	createIfNotExist("Document")
	createIfNotExist("Image")
	createIfNotExist("Music")
	createIfNotExist("Others")
	
	moveFile(imageFiles,"Image")
	moveFile(documentFiles,"Document")
	moveFile(musicFiles,"Music")
	moveFile(otherFiles,"Others")

	sleep(2)
	print(f"[+] Total {clutterCount} Files Moved Now :)")

