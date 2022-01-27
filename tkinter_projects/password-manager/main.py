from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
FONT_SIZE = 15
FONT = (FONT_NAME, FONT_SIZE, "bold")
DEFAULT_EMAIL = "kiranlvs93@gmail.com"


# ---------------------------- SEARCH MECHANISM ------------------------------- #
def search():
    """
    Search for a website and fetch the credentials
    :return:
    """
    search_keyword = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=search_keyword,
                                message=f"Email:{data[search_keyword]['email']}\nPassword:{data[search_keyword]['password']}")
    except (FileNotFoundError, KeyError) as e:
        messagebox.showerror(title="No Data Found", message=f"Info not found for {search_keyword}. Error::{e}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generate password randomly
    Password includes 6-10 letters, 2-4 symbols and 2-4 numbers
    :return:
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers,
                                                                                                            nr_numbers)
    random.shuffle(password_list)
    password = "".join(password_list)

    # Copy the password to clipboard
    pyperclip.copy(password)

    # Delete the existing word in password field and insert the generated password
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_details_to_file(user_inp, file_data):
    """
    While adding a website's data, check if the data already exists.
    If data is already present, prompt the user that the data is already present
    If user wants to overwrite, update the password else take the user back to the screen
    :param user_inp:
    :param file_data:
    :return: Response from the message box
    """
    overwrite = True
    if website_entry.get() in file_data.keys():
        overwrite = messagebox.askokcancel("Duplicate Entry",
                                           "Website already present in the file. Do you want to overwrite?")
    if overwrite:
        with open("passwords.json", "w") as data_file:
            file_data.update(user_inp)
            json.dump(file_data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Save Successful", message="Password saved successfully")


def save_form_data():
    """
    Save the form data if all the fields are filled.
    Even if one of the fields is blank, show the user an error message
    If all the fields are filled, then ask for confirmation. If OK, append data to the file.
    :return:
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    user_inp = {website: {"email": email, "password": password}}

    if not all([len(website), len(email), len(password)]):
        messagebox.showerror(title="Empty Fields Detected",
                             message="Dont leave any field empty. All fields are mandatory")
    else:
        is_ok = messagebox.askokcancel("Confirmation",
                                       f"Details you entered are\n\n{website}\n{email}\n{password}"
                                       f"\n\n Proceed with Save?")
        if is_ok:
            file_data = {}
            try:
                with open("passwords.json", "r") as data_file:
                    file_data = json.load(data_file)
            except FileNotFoundError:
                pass
            finally:
                write_details_to_file(user_inp, file_data)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20)

# Adding canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Adding Labels
website_label = Label(text="Website:", )
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Adding the entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
# Set focus on launch
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
# Insert a pre-defined text
email_entry.insert(index=0, string=DEFAULT_EMAIL)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Adding buttons
search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column=2, sticky="EW")

gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=35, command=save_form_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
