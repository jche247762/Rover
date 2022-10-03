import os
from loader import *

def quit_game():
	"""
	Will quit the program
	"""
	exit()

def menu_help():
	"""
	Displays the help menu of the game
	"""
	print()
	print("START <level file> - Starts the game with a provided file.")
	print("QUIT - Quits the game")
	print("HELP - Shows this message")
	print()

def menu_start_game(filepath):
	"""
	Will start the game with the given file path
	"""
	if not os.path.exists(filepath):
		print()
		print("Level file could not be found")
		print()
	else:
		structure_correct, pt, rov = load_level(filepath)
		if not structure_correct:
			print()
			print("Unable to load level file")
			print()
		else:
			while True:
				a = input()
				if a == "FINISH":
					print()
					print("You explored {0:}% of {1:}".format(int(pt.ratio * 100 / (pt.width * pt.height)), pt.name))
					print()
					exit()
				if a == "STATS":
					print()
					print("Explored: {}%".format(int(pt.ratio * 100 / (pt.width * pt.height))))
					print("Battery: {0:}/100".format(rov.battery))
					print()
					continue
				if "MOVE" in a:
					direct = a.strip().split(" ")[1]
					cycles = int(a.strip().split(" ")[2])
					if not direct == "N" and not direct == "E" and not direct == "S" and not direct == "W": continue
					if cycles <= 0: continue
					rov = pt.explore(direct, cycles, rov)

				if "SCAN" in a:
					mode = a.strip().split(" ")[1]
					if mode == "shade":
						pt.scan_shade(rov.x, rov.y)
					elif mode == "elevation":
						pt.scan_elevation(rov.x, rov.y, rov.elv)
					else:
						print("Cannot perform this command")
				if "WAIT" in a:
					cycles = a.strip().split(" ")[1]
					if not pt.tiles[rov.x][rov.y].is_shaded():
						rov.wait(cycles)

def menu():
	"""
	Start the menu component of the game
	"""
	a = input()
	if "START" in a:
		filepath = a.split(' ')[1]
		menu_start_game(filepath)
	elif a == "HELP":
		menu_help()
	elif a == "QUIT":
		quit_game()
	else:
		print()
		print('No menu item')
		print()
menu()

		
		
		
		
