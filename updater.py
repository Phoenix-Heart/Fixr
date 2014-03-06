'script to modify py files which use the wx library, but incorrectly identify the version installed'
'This is essentially an elaborate replace all. You can, therefore, modify the strings in use for your purpose.. '
'simply by replacing the old_str and new_str lists with your own'


import os
root = 'D:\gui2py\gui2py'
ext = '.py'
os.chdir(root)
append = ''
old_str = ["wx.VERSION < (2, 9, 5)","wx.VERSION > (2, 9, 5)"]
new_str = ["wx.version().find('classic')!=-1","wx.version().find('classic')==-1"]
# todo: implement run with a loop
def run(current_dir):
	os.chdir(current_dir)
	dirs = list()
	for file_ in os.listdir('.'):
		if os.path.isdir(file_):
			dirs.append(file_)
		elif file_.endswith(ext):
			convert(file_)
	for dr in dirs:
		run(dr)
		os.chdir('..')

def convert(_file):
	try:
		f = open(_file)
		_newfile = new_filename(_file)
		r = open(_newfile, 'w')
		for line in f:
			for old,new in zip(old_str,new_str):
				line = line.replace(old,new)
			r.write(line)
		f.close()
		r.close()
		os.remove(_file)
		os.rename(_newfile,_file)
	except Exception, e:
		# TODO: better exception handling
		print e

def new_filename(old_name):
	'create a new version of the file with a modified filename'   
	ext_pos = old_name[::-1].find('.')
	name = old_name[:len(old_name)-ext_pos]
	_name = name+append+ext 
	return _name
	# end new_filenames()


if __name__ == '__main__':
	run(root)