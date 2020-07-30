from tkinter import *

root = Tk()
root.title("calculator")
root.geometry("410x300")

e = Entry(root)
e.grid(row=4, column=5)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))
# all buttons currently add numbers together because the functions are identical and button_equal only adds


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


zerobutton = Button(root, text="0", padx=25, pady=25,command=lambda: button_click(0)).grid(row=4, column=2)
onebutton = Button(root, text="1", padx=25, pady=25, command=lambda: button_click(1)).grid(row=1, column=1)
twobutton = Button(root, text="2", padx=25, pady=25, command=lambda: button_click(2)).grid(row=1, column=2)
threebutton = Button(root, text="3", padx=25, pady=25, command=lambda: button_click(3)).grid(row=1, column=3)
fourbutton = Button(root, text="4", padx=25, pady=25, command=lambda: button_click(4)).grid(row=2, column=1)
fivebutton = Button(root, text="5", padx=25, pady=25, command=lambda: button_click(5)).grid(row=2, column=2)
sixbutton = Button(root, text="6", padx=25, pady=25, command=lambda: button_click(6)).grid(row=2, column=3)
sevenbutton = Button(root, text="7", padx=25, pady=25, command=lambda: button_click(7)).grid(row=3, column=1)
eightbutton = Button(root, text="8", padx=25, pady=25, command=lambda: button_click(8)).grid(row=3, column=2)
ninebutton = Button(root, text="9", padx=25, pady=25, command=lambda: button_click(9)).grid(row=3, column=3)


clearbutton = Button(root, text="C", padx=25, pady=25, command=button_clear).grid(row=4, column=1)
equalbutton = Button(root, text="=", padx=25, pady=25, command=button_equal).grid(row=4, column=3)


plusbutton = Button(root, text="+", padx=25, pady=25, command=button_add).grid(row=1, column=4)
minusbutton = Button(root, text="-", padx=25, pady=25, command=button_subtract).grid(row=2, column=4)
miltiplybutton = Button(root, text="x", padx=25, pady=25, command=button_multiply).grid(row=3, column=4)
dividebutton = Button(root, text="/", padx=25, pady=25, command=button_divide).grid(row=4, column=4)


root.mainloop()
