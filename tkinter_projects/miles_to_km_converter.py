from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("Miles to KM Converter")
window.config(padx=50, pady=50)


def convert_miles_to_km():
    converted_value["text"] = str(int(inp_in_miles.get()) * 1.60934)


inp_in_miles = Entry()
inp_in_miles.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="=", font=("Arial", 10, "bold"))
is_equal_label.grid(row=1, column=1)

converted_value = Label(text="0.00", font=("Arial", 10, "bold"))
converted_value.grid(row=2, column=1)

miles_label = Label(text="KM")
miles_label.grid(row=2, column=2)

button = Button(text="Convert", command=convert_miles_to_km)
button.grid(row=3, column=1)

window.mainloop()
