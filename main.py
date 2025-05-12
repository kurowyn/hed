import sys, os, string

VIEW_COMMANDS = ('u', 'd', 'x')

clear_screen = lambda: os.system('clear' if os.name == 'posix' else 'cls')

if len(sys.argv) != 2:
  print('usage: python main.py (filename)')
	exit(1)

try:
	with open(sys.argv[1]) as f:
		lines = f.readlines()
except:
	print(f"ERROR: file {sys.argv[1]} doesn't exist!")
	exit(1)

visual_lines = lines[:]

def parse_command(command):
	# Valid commands, for now, are of the format: nd, nu, nx, where n is a single digit 
	# positive integer.

	command = list(command.replace(' ', ''))

	if len(command) > 2:	
		return (None, None)
	elif len(command) == 1 and command[0] in VIEW_COMMANDS:
		return (1, command[0])
	elif len(command) == 2 and command[0] in string.digits and command[1] in VIEW_COMMANDS:
		return (int(command[0]), command[1])
	return (None, None)



previous_command = (None, None)

while True:
	clear_screen()

	print(*visual_lines, sep = '', end = '')

	command = parse_command(input())

	occurrence, option = command if command != (None, None) else previous_command

	if option != None:
		for i in range(occurrence):
			match option:
				case 'u':
					try:
						visual_lines.pop()
					except:
						pass
				case 'd':
					if visual_lines != lines:
						visual_lines.append(lines[len(visual_lines)])
					else: 
						break
				case 'x':
					print('Exiting...')
					exit(0)
				case _:	
					break

	previous_command = occurrence, option
