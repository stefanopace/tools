dice = [dice.strip().split('\n') for dice in ['''
╭───────╮
│       │
│   ◉   │
│       │
╰───────╯
''','''
╭───────╮
│     ◉ │
│       │
│ ◉     │
╰───────╯
''','''
╭───────╮
│     ◉ │
│   ◉   │
│ ◉     │
╰───────╯
''','''
╭───────╮
│ ◉   ◉ │
│       │
│ ◉   ◉ │
╰───────╯
''','''
╭───────╮
│ ◉   ◉ │
│   ◉   │
│ ◉   ◉ │
╰───────╯
''','''
╭───────╮
│ ◉   ◉ │
│ ◉   ◉ │
│ ◉   ◉ │
╰───────╯
''']]

def terminal_width():
	import fcntl, termios, struct
	th, tw, hp, wp = struct.unpack('HHHH',
		fcntl.ioctl(0, termios.TIOCGWINSZ,
		struct.pack('HHHH', 0, 0, 0, 0)))
	return tw

def print_dices(faces):
	cols = terminal_width()
	dice_width = 10
	dices_in_a_row = cols // dice_width
	for i in range(0, len(faces), dices_in_a_row):
		print_row(faces[i: i + dices_in_a_row])

def print_row(faces):
	for line in range(5):
		for face in faces:
			print(dice[face - 1][line], end=' ')
		print()

