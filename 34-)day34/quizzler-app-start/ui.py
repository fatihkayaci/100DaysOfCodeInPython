from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, background = THEME_COLOR)

        self.score = Label(text = "Score: 0", font = ("Arial", 10, "bold"), background = THEME_COLOR, fg = "white")
        self.score.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250, background = "white")
        self.canvas.grid(row = 1, column = 0, columnspan = 2)
        self.question_text = self.canvas.create_text(150, 125, text = "Amazon acquared twitch in august 2014 for $970 million dollars.", font = ("Arial", 20, "italic"), width = 250)

        self.true_image = PhotoImage(file = "images/true.png")
        self.correct_button = Button(image = self.true_image, background = THEME_COLOR, highlightthickness = 0, command = self.false_pressed)
        self.correct_button.grid(row = 2, column = 0)
        self.false_image = PhotoImage(file = "images/false.png")
        self.incorrect_button = Button(image = self.false_image, background = THEME_COLOR, highlightthickness = 0, command = self.false_pressed)
        self.incorrect_button.grid(row = 2, column = 1)

        self.next_question_get()
        self.window.mainloop()
    
    def next_question_get(self):
        self.canvas.config(background = "white")
        if self.quiz.still_has_questions():        
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "you have reached the end of the quiz.")
            self.correct_button.config(state = "disabled")
            self.incorrect_button.config(state = "disabled")
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background = "green")
        else:
            self.canvas.config(background = "red")
        self.window.after(1000, self.next_question_get)
        