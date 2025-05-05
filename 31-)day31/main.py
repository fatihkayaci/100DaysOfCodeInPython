from tkinter import *
from random import *
import pandas as pd
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = None
to_learn = None
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient = "records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(background_image, image = front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(background_image, image = back_image)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")

def is_know():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, background = BACKGROUND_COLOR)
flip_timer= window.after(3000, flip_card)

canvas = Canvas(width = 800, height = 526, background = BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file = "images/card_front.png")
back_image = PhotoImage(file = "images/card_back.png")

background_image = canvas.create_image(400, 263, image = front_image)
card_title = canvas.create_text(400, 150, text = "", font= ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font= ("Ariel", 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan = 2)


wrong = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image = wrong, highlightthickness = 0, command = next_card)
wrong_button.grid(column = 0, row = 1)

right = PhotoImage(file = "images/right.png")
right_button = Button(image = right, highlightthickness = 0, command = is_know)
right_button.grid(column = 1, row = 1)
next_card()
window.mainloop()