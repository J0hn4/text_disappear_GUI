import time
from tkinter import *
from tkinter import messagebox
import threading

timer_speed = 0

#resets timer to 10
def add_time(*args):
    global timer_speed
    timer_speed = 10

#everytime text is entered, the 10 second countdown is initiated, and text is deleted in the box after 10 seconds
def countdown(*args):
    global timer_speed
    timer = True
    timer_speed = 10
    while timer:
        time.sleep(1)
        timer_speed -= 1
        text_entry_box.bind("<Key>", add_time)
        if timer_speed == 0:
            text_entry_box.delete("1.0", "end")


# ------------------------------------- GUI Configuration -----------------------------------------#

# creating the tkinter window
window = Tk()
window.title("Disappearing Text App")
window.minsize(width=1000, height=700)
window.configure(bg='grey')

#create heading lable for typing box
text_entry_label = Label(window, text="Your text disappears if you stop typing for more than 10 seconds. Start typing below:")
text_entry_label.grid(row=0, column=1)
text_entry_label.configure(font=("Arial", 30, "bold"), bg ='grey')

#create box for typing in text
text_entry_box = Text(height=40, width=150, wrap="word")
text_entry_box.grid(row=1, column=1, ipadx=100)
text_entry_box.configure(font=("Arial", 15, "normal"), bg='#856ff8')

#when typing, executes countdown function which adds another 10 seconds to the countdown
text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())


window.mainloop()