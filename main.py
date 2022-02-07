import pyperclip
import keyboard
from time import sleep
from os import system
from rich.console import Console
from rich.traceback import install
from rich.prompt import Confirm
import sys
install()

console = Console()

def waitForPaste():
	while True:
		if keyboard.is_pressed('ctrl'):
			if keyboard.is_pressed('v'):
				while keyboard.is_pressed('v'):
					pass
				return True
		elif keyboard.is_pressed('esc'):
			sys.exit()


def waitForCopy():
	while True:
		if keyboard.is_pressed('ctrl'):
			if keyboard.is_pressed('c'):
				while keyboard.is_pressed('c'):
					pass
				return True
		elif keyboard.is_pressed('esc'):
			sys.exit()

def main():
	system('cls')
	console.print('CSV Paster V1.2', justify="center")
	console.print('[+] Copy the list', style="green")
	waitForCopy()

	pasteDump = pyperclip.paste() #Get Contents of the CSV File

	RowSplit = pasteDump.split('\n') #Split up the CSV Into Rows
	database = [] #Define the varible that will hold the database
	for i in range(0, len(RowSplit)):
		database.append([]) #Create an empty list to every row

	for	i in RowSplit:
		tempList = i.split('\t') 
		for i2 in tempList: #Split the rows up into collums and put them in the correct lists in the database
			database[RowSplit.index(i)].append(i2)

	for i1 in database:
		for i2 in i1: #Copy each cell in sequence and wait for the user to paste.
			pyperclip.copy(i2)
			system('cls')
			console.print("[+] Ready to Paste " + i2, style="green")
			#print(i2)
			waitForPaste()

	system('cls')
	pyperclip.copy("Sequence Complete - Please Stop Pasting")
	if Confirm.ask("[+] Sequence Complete, Would you like to go again?"):
		main()
	else:
		console.print('[+] Program Exiting', style="red")


main()
