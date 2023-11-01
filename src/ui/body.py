from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from util.console import *
from util.file import *

from pynput import keyboard as kbd

class Body:

	def __init__(self, file: File):
		self.file = file
		self.contents = file.read()
		self.max_lines = console.height - (MIN_SIZE*2) - 2
		self.display = 0

	def __rich__(self):
		source = Table(show_header=False, show_lines=False, show_edge=False, padding=(0, 0), expand=True)
		source.add_column(header="Row Number", width=5)
		source.add_column(header="Text", width=console.width-8)
		
		idx = 0
		lines = self.contents[self.display:]
		for idx, line in enumerate(lines):
			if not idx < self.max_lines:
				break
			line_num = self.display + idx + 1
			source.add_row(Text(str(line_num), style="cyan"), Text(line, tab_size=4))

		return Panel(source)

	def on_press(self, key):
		key_t = type(key).__name__

		if key_t == "Key":
			if key == kbd.Key.esc:
				return False
			if key == kbd.Key.down:
				self.display += 1 if self.display != len(self.contents)-1 else 0
			if key == kbd.Key.up:
				self.display -= 1 if self.display != 0 else 0
		if key_t == "KeyCode":
			if str(key.char) == "\x13":	
				self.file.write(self.contents)