import util.cd as cd
import util.colours as colours

class File:
	def __init__(self, name, root):
		self.name = name
		self.path = cd.find(name, "file", root)
		if self.path == "":
			raise FileNotFoundError(f"{colours.red}{name} does not exist!{colours.reset}")
	
	def read(self):
		contents = ""
		with open(self.path, "r") as file:
			contents = file.read().strip()
		
		contents = contents.split(sep="\n")
		return contents
	
	def write(self, contents):
		with open(self.path, "w") as file:
			file.writelines(contents)

		return