from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from util.console import console
from util.file import *

MIN_SIZE = 3

class Header:
	def __init__(self, file: str):
		self.file = file

	def __rich__(self):
		title = Text(f"Currently editing: {self.file}", style="cyan", justify="center")
		return Panel(title)

class Footer:
	def __rich__(self):
		keybinds = [
			Text("Ctrl+S to save", style="cyan", justify="center"),
			Text("Ctrl+Q to quit", style="cyan", justify="center"),
			Text("Ctrl+H to display all keybinds", style="cyan", justify="center"),
		]

		table = Table.grid(expand=True)
		column_width = (console.width-4)//3
		table.add_column(header="", width=column_width)
		table.add_column(header="", width=column_width)
		table.add_column(header="", width=column_width)

		table.add_row(keybinds[0], keybinds[1], keybinds[2])

		return Panel(table, height=MIN_SIZE)

class body:
	def __init__(self, file: File):
		self.file = file
		self.content = file.read()
		self.max_lines = console.height - (MIN_SIZE*2) - 2
		self.display = self.content[:self.max_lines]

	def __rich__(self):
		source = Table(show_header=False, show_lines=False, show_edge=False, expand=True)
		source.add_column(header="Row Number", width=MIN_SIZE)
		source.add_column(header="Text", width=console.width-MIN_SIZE)

		idx = 0

		for idx, line in enumerate(self.content):
			strdx = Text(str(idx), style="cyan")
			line = Text(line)
			source.add_row(strdx, line)

		self.max_lines - (idx + 1)

		

		return Panel(source)

def set_layout():
	layout = Layout(name="root")

	layout.split(
		Layout(name="header", size=MIN_SIZE),
		Layout(name="body", minimum_size=5),
		Layout(name="footer", size=MIN_SIZE),
	)
	
	return layout