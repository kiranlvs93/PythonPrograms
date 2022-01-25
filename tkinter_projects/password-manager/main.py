from tkinter import *

FONT_NAME = "Courier"
FONT_SIZE = 15
FONT = (FONT_NAME, FONT_SIZE, "bold")
DEFAULT_EMAIL = "kiranlvs93@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

# Adding canvas
canvas = Canvas(width=250, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Adding Labels
website_label = Label(text="Website:", )
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Adding the entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
# Set focus on launch
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
# Insert a pre-defined text
email_entry.insert(index=0, string=DEFAULT_EMAIL)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Adding buttons
gen_password_btn = Button(text="Generate Password", width=30, command=generate_password)
gen_password_btn.grid(row=4, column=1, columnspan=2)

add_btn = Button(text="Add", width=30, command=generate_password)
add_btn.grid(row=5, column=1, columnspan=2)

window.mainloop()
