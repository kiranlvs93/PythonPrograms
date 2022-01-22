from tkinter import *


def button_clicked():
    """
    Update the click count when button is clicked
    :return:
    """
    global count
    count += 1
    click_count["text"] = f"Click count:: {count}"
    message["text"] = inp.get()
    inp.delete(0, 'end')


# Window
window = Tk()
window.minsize(width=300, height=300)
window.title("Sample Window")

# Labels
click_count = Label(text="Button Clicks Count", font=("Arial", 15, "bold"))
click_count.pack()

message = Label(text="Input Msg!!", font=("Arial", 10))
message.pack()

# Button
button = Button(text="Click Me", font=("Arial", 10, "bold"), command=button_clicked)
button.pack()
count = 0

# Entry
inp = Entry(width=20, relief="raised")
inp.pack()

window.mainloop()
