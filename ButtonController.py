from Mode_0 import Mode_0

def modeSelector(bit_0, bit_1, bit_2):
	if bit_0:
		if bit_1:
			if bit_2:
				return 7
			else:
				return 6
		else:
			if bit_2:
				return 5
			else:
				return 4
	else:
		if bit_1:
			if bit_2:
				return 3
			else:
				return 2
		else:
			if bit_2:
				return 1
			else:
				return 0

val = Mode_0()
val.button_3()