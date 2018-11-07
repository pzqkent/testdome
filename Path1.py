# Write a function that provides change directory (cd) function for an abstract file system.

# Notes:

# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.
# For example:

		# path = Path('/a/b/c/d')
		# path.cd('../x')
		# print(path.current_path)



class Path:
	def __init__(self,path):
		self.current_path = path

	def cd(self,new_path):
		i = 0
		new_pathList = new_path.split('/')
		pathLength = len(new_pathList)
		pathList = self.current_path.split('/')
		print(new_pathList)
		print(pathList)
		if new_pathList[0] == '':
			'''
			用于对应绝对路径。即如果新路径经过分割后第一位为空，则清空老的路径，并将新的路径
			头添加进去。	
			'''
			pathList = []
			pathList.append('/' + new_pathList[1])
			i += 2
		while i < pathLength:
			if new_pathList[i] == '..':
				'''
				用于应对相对路径
				'''
				pathList.pop(-1)
				print('relative address',pathList)
			else:
				pathList.append(new_pathList[i])
			i += 1
		self.current_path = '/'.join(pathList)

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

