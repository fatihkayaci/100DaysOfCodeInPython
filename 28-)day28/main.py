from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
demo_text = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer", fg = GREEN)
    tic_label.config(text = "")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global demo_text
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "Break", fg=PINK)
        demo_text += "✅"
        tic_label.config(text = demo_text)
    else:
        count_down(work_sec)
        title_label.config(text = "Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_second = count % 60
    
    if count_second < 10:
        count_second = f"0{count_second}"
    
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# canvas creater
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/pc/Desktop/100daysofcode/100DaysOfCodeInPython/28-)day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(width=4, height=1, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(width=4, height=1, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tic_label = Label(fg=GREEN, background=YELLOW)
tic_label.grid(column=1, row=3)

window.mainloop()