# importing tkinter
from re import A
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import bgcolor, color

# colors
color1 = "#000000"  # black
color2 = "#fcfcfc"  # white
color3 = "#3052b8"  # smoothblue
color4 = "#969aa3"  # gray
color5 = "#f7942a"  # orange

window = Tk()
window.title("calculadora")
window.geometry("235x270")
window.config(bg=color1)

# creating frames
frame_window = Frame(window, width=235, height=50, bg=color3)
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# variable all values

all_values = ''


# creating label
value_text = StringVar()

# creating functions


def enter_values(event):

    global all_values

    all_values = all_values + str(event)


# passing values to the screen
    value_text.set(all_values)


# function to calculate
def calculate():
    global all_values
    result = eval(all_values)
    print(result)

    value_text.set(str(result))


# function to clear screen
def clear_screen():
    global all_values
    all_values = ""
    value_text.set("")


app_label = Label(frame_window, textvariable=value_text, width=16, height=2,
                  padx=7, relief=FLAT, anchor="e", font="Ivy 18", bg=color3, fg=color2)
app_label.place(x=0, y=0)


# creating buttons

b_1 = Button(frame_body, command=clear_screen, text="C", width=17, height=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, command=lambda: enter_values('%'), text="%", width=8, height=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=124, y=0)

b_3 = Button(frame_body, command=lambda: enter_values('/'), text="➗", width=4, height=2, bg=color5,
             fg=color2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=188, y=0)

b_4 = Button(frame_body, command=lambda: enter_values('1'), text="1", width=8, height=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=41)

b_5 = Button(frame_body, command=lambda: enter_values('2'), text="2", width=8, height=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=62, y=41)

b_6 = Button(frame_body, command=lambda: enter_values('3'), text="3", width=8, heigh=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=124, y=41)

b_7 = Button(frame_body, command=lambda: enter_values('4'), text="4", width=8, heigh=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=80)

b_8 = Button(frame_body, command=lambda: enter_values('5'), text="5", width=8, heigh=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=62, y=80)
b_9 = Button(frame_body, command=lambda: enter_values('6'), text="6", width=8, heigh=2, bg=color4,
             fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=124, y=80)

b_10 = Button(frame_body, command=lambda: enter_values('7'), text="7", width=8, heigh=2, bg=color4,
              fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=119)

b_11 = Button(frame_body, command=lambda: enter_values('8'), text="8", width=8, heigh=2, bg=color4,
              fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_11.place(x=62, y=119)

b_12 = Button(frame_body, command=lambda: enter_values('9'), text="9", width=8, heigh=2, bg=color4,
              fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=124, y=119)

b_13 = Button(frame_body, command=lambda: enter_values('*'), text="✖", width=4, heigh=2, bg=color5,
              fg=color2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=188, y=41)

b_14 = Button(frame_body, command=lambda: enter_values('+'), text="➕", width=4, heigh=2, bg=color5,
              fg=color2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_14.place(x=188, y=80)

b_15 = Button(frame_body, command=lambda: enter_values('-'), text="➖", width=4, heigh=2, bg=color5,
              fg=color2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_15.place(x=188, y=119)

b_16 = Button(frame_body, command=calculate, text="=", width=5, heigh=2, bg=color5,
              fg=color2, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_16.place(x=188, y=169)

b_17 = Button(frame_body, command=lambda: enter_values('.'), text=".", width=6, heigh=2, bg=color4,
              fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=169)

b_18 = Button(frame_body, command=lambda: enter_values('0'), text="0", width=12, heigh=2, bg=color4,
              fg=color1, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_18.place(x=-4, y=169)


window.mainloop()
