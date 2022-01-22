from tkinter import *

window = Tk()
window.minsize(width=300, height=300)
window.title("Sample Window")
click_count = Label(text="Button Clicks Count", font=("Arial", 15, "bold"))
click_count.pack()

message = Label(text="Input Msg!!", font=("Arial", 10))
message.pack()


def button_clicked():
    global count
    count += 1
    click_count["text"] = f"Click count:: {count}"
    message["text"] = inp.get()
    inp.delete(0, 'end')


button = Button(text="Click Me", font=("Arial", 10, "bold"), command=button_clicked)
button.pack()
count = 0

inp = Entry(width=20, relief="raised")
inp.pack()

window.mainloop()
