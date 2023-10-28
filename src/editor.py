from util.console import console
from util.file import *
import ui

def Editor(file: File):
	editor = ui.set_layout()
	editor["header"].update(ui.Header(file.name))
	editor["footer"].update(ui.Footer())
	console.print(editor)
	
	return 0

if __name__ == "__main__":
	editor = ui.set_layout()
	editor["header"].update(ui.Header("editor.py"))
	editor["footer"].update(ui.Footer())
	editor["body"].update(ui.body(File("editor.py", "editor")))
	console.print(editor)