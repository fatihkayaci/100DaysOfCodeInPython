from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers 
    shuffle(password_list)

    password = "".join(password_list)
    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_text.get()
    email = email_text.get()
    password = password_text.get()
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty!")        
    else:
        is_ok = messagebox.askokcancel(title = web, message = f"These are the details entered: \n Email: {email}"
                                                    f"\n Password: {password} \n Is it oke to save?" )
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{web} | {email} | {password} \n")
                web_text.delete(0, END)
                password_text.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

# create window
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# create canvas and logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file = "/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/29-)day29/logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column = 1, row = 0)

# --------------------- create widgets -----------------------------
# --------------------- Labels ----------------------------
web_label = Label(text = "Web Site:")
web_label.grid(column = 0, row = 1)
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# --------------------- Texts --------------------------
web_text = Entry(width = 35)
web_text.grid(column = 1, row = 1, columnspan = 2)
web_text.focus()
email_text = Entry(width = 35)
email_text.insert(0, "fatihkayaci@yahoo.com")
email_text.grid(column = 1, row = 2, columnspan = 2)
password_text = Entry(width = 21)
password_text.grid(column = 1, row = 3, columnspan = 1)

# --------------------- Buttons -----------------------
password_genereta_button = Button(text = "Generate Password", command=generate_password)
password_genereta_button.grid(column = 2, row = 3)

add_button = Button(width = 36, text = "Add", command=save)
add_button.grid(column = 1, row = 4, columnspan = 2)




window.mainloop()