from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from util.console import *

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
			Text("Esc to quit", style="cyan", justify="center"),
			Text("Ctrl+H to display all keybinds", style="cyan", justify="center"),
		]

		table = Table.grid(expand=True)
		column_width = (console.width-4)//3
		table.add_column(header="", width=column_width)
		table.add_column(header="", width=column_width)
		table.add_column(header="", width=column_width)

		table.add_row(keybinds[0], keybinds[1], keybinds[2])

		return Panel(table, height=MIN_SIZE)

def set_layout():
	layout = Layout(name="root")

	layout.split(
		Layout(name="header", size=MIN_SIZE),
		Layout(name="body", minimum_size=5),
		Layout(name="footer", size=MIN_SIZE),
	)
	
	return layout