from os	import listdir,getcwd,remove,rmdir

from os.path import isfile, join

print getcwd() # getcwd gete the current path
files = [f for f in listdir(getcwd()) if isfile(join(getcwd(),f))] # listdir(path) returns a list of files and dirs in the given path

py = []
pyc = []

for f in files:
	tmp = f.split('.')
	if(tmp[-1]=='py'):
		py.append(tmp[0])
	if(tmp[-1]=='pyc'):
		pyc.append(tmp[0])

print py
print pyc

for name in py:
	filename = name+'.py'
	print join(getcwd(),filename)
	print isfile(join(getcwd(),filename))