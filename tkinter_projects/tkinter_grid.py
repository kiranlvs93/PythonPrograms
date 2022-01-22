from tkinter import *

count = 0

# Grid is relative to each other
def button_clicked():
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
click_count.grid(row=0, column=0)

message = Label(text="Input Msg!!", font=("Arial", 10))
message.grid(row=0, column=2)

# Button
button = Button(text="Click Me", font=("Arial", 10, "bold"), command=button_clicked)
button.grid(row=1, column=1)

# Entry
inp = Entry(width=20, relief="raised")
inp.grid(row=4, column=4)

window.mainloop()
