import sys, os, string

VIEW_COMMANDS = ('u', 'd', 'x')

clear_screen = lambda: os.system('clear' if os.name == 'posix' else 'cls')

# A little hacky, but whatevs.
err_msg = lambda msg, code: print(msg) or (exit(code) and True)

# Some error handling.
if len(sys.argv) != 2:
	err_msg('usage: python main.py (filename)', 1)
try:
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		visual_lines = lines[:]
except:
	err_msg(f"ERROR: file {sys.argv[1]} doesn't exist!", 1)

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

	if not all(command := parse_command(input())):
		command = previous_command

	match command:
		case (occurrence, 'u'):
			if visual_lines[1:]:
				visual_lines = visual_lines[:len(visual_lines) - occurrence]
		case (occurrence, 'd'):
				visual_lines.extend(lines[len(visual_lines):len(visual_lines) + occurrence])
		case (occurrence, 'x'):
				print('Exiting...')
				exit(0)
		case _:
			continue

	previous_command = command
