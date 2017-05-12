from Tkinter import *
from ButtonController import ButtonController
buttCon = ButtonController()



buttons = []
def add_callback(control, fun):
    def inner():
        return fun(control)
    control['command'] = inner

def buttonPress(butt):
    if not butt.is_up:
        butt.configure(bg='red')
    else:
        butt.configure(bg='white')
    # buttControl.switchFlipped(butt.id, butt.is_up)
    buttCon.switchFlipped(butt.id)
    butt.is_up = not butt.is_up


root = Tk()
buttons = []
# for i in range(0, 9):
#     buttons.append(Button(root, text=i, command="buttonPress"))
#     buttons[i].grid(column=3, row = )

for curRow in range(3):
    for curCol in range(3):
        b = Button( text='', bg="white", height= 10, width=10)
        b.id = curRow * 3 + curCol
        b.is_up = False
        add_callback(b, buttonPress)
        b.grid(row=curRow, column=curCol)
        buttons.append(b)




mainloop()
