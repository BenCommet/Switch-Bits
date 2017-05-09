from Mode_0 import Mode_0
from Mode_1 import Mode_1
from Mode_2 import Mode_2
from Mode_3 import Mode_3
from Mode_4 import Mode_4
from Mode_5 import Mode_5
from Mode_6 import Mode_6
from Mode_7 import Mode_7


class ButtonController:
	def __init__(self):
		print("duck")
		self.buttons = [False, False, False, False, False, False, False, False, False]
		self.currentMode = Mode_0()

	def switchFlipped(self, switch_ID, is_on):
		self.buttons[switch_ID] = is_on
		if switch_ID < 3:
			self.modeSelector(self.buttons[0], self.buttons[1], self.buttons[2])
		else:
			if switch_ID == 3:
				self.currentMode.button_3(is_on)
			elif switch_ID == 4:
				self.currentMode.button_4(is_on)
			elif switch_ID == 5:
				self.currentMode.button_5(is_on)
			elif switch_ID == 6:
				self.currentMode.button_6(is_on)
			elif switch_ID == 7:
				self.currentMode.button_7(is_on)
			elif switch_ID == 8:
				self.currentMode.button_8(is_on)


	def modeSelector(self, bit_0, bit_1, bit_2):
		if bit_0:
			if bit_1:
				if bit_2:
					self.currentMode = Mode_7()
				else:
					self.currentMode = Mode_6()
			else:
				if bit_2:
					self.currentMode = Mode_5()
				else:
					self.currentMode = Mode_4()
		else:
			if bit_1:
				if bit_2:
					self.currentMode = Mode_3()
				else:
					self.currentMode = Mode_2()
			else:
				if bit_2:
					self.currentMode = Mode_1()
				else:
					self.currentMode = Mode_0()
