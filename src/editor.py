import sys
import os

from pynput import keyboard as kbd
from rich.live import Live
from rich import print

from util.kbd_interrupt import DelayedKeyboardInterrupt
from util.console import console
from util.file import *
import ui.ui as ui
from ui.body import *

def Editor(file: File):
	header = ui.Header(file.name)
	body = Body(file)
	footer = ui.Footer()

	editor = ui.set_layout()
	editor["header"].update(header)
	editor["footer"].update(footer)
	editor["body"].update(body)
	
	with Live(editor, refresh_per_second=100):
		with kbd.Listener(on_press=body.on_press) as listener:
			listener.join()

	return 0

if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			print("[bold red]:warning-emoji:  PROPER USAGE: python src/editor.py [FILE][/]")
			sys.exit(1)
		file_name = sys.argv[1]
		p, root = os.path.split(os.getcwd())
		file = File(file_name, root)
		with DelayedKeyboardInterrupt():
			Editor(file)
			sys.exit(0)
	except KeyboardInterrupt:
		pass