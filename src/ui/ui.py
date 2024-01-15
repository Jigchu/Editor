from rich.console import Group
from rich.panel import Panel

from util.console import console

class element:
	def __init__(self):
		self.size = (console.width, 3)
		self.content = ""
	
	def set_content(self):
		self.content = Group(
			Panel("Hello World :)")
		)

	def __rich__(self):
		return Panel(self.content, width=self.size[0], height=self.size[1])