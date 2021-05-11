#Copy all python files to Python folder

import os
import shutil

#print(os.getcwd()) --> We are here only

dest = os.path.join(os.getcwd(),"Python")

def copy_files_from_folder(fold):
	for f in os.listdir(fold):
		if f[0]!='.':
			if os.path.isfile(os.path.join(fold,f)):
				if f[-2:]=="py":
					try:
						shutil.copy(os.path.join(fold,f),dest)
					except:
						pass
			else:
				copy_files_from_folder(os.path.join(fold,f))



print(os.getcwd())
copy_files_from_folder(os.getcwd())
