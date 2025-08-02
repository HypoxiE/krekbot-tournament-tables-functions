
import pyperclip

def addToClipBoard(text):
    pyperclip.copy(text)


with open('public_table_function.txt', encoding='utf-8') as f:
	addToClipBoard(f.read().replace("\t", "").replace("\n", ""))