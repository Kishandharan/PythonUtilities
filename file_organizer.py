import os
import shutil
import sys
#############################################
path = sys.argv[1]
ext = sys.argv[2]
dir_name = f"{ext} files"
os.chdir(path)
list1 = os.listdir()
if not os.path.isdir(dir_name):
	os.mkdir(dir_name)
for i in list1:
	if (i.endswith(ext)) and (os.path.isfile(i)):
		shutil.move(i, path+"\\"+dir_name)
