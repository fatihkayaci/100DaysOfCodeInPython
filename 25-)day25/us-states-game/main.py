import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# first way
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
print(all_states)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# second way

# pencil = turtle.Turtle()
# pencil.penup()
# pencil.hideturtle()
# data_file = pd.read_csv("50_states.csv")
# another_answer = screen.textinput(title="Guess The State", prompt="What's another state's name?")
# another_answer = another_answer.lower()

# score = 0
# game_is_on = True
# while game_is_on:
#     matched_row = data_file[data_file["state"].str.lower() == another_answer]
#     matched_rowx = float(matched_row.x)
#     matched_rowy = float(matched_row.y)

#     if not matched_row.empty:
#         pencil.goto(matched_rowx, matched_rowy)
#         pencil.write(another_answer, move=True, align='center', font=('Arial', 8, 'normal'))
#         score += 1
#     another_answer = screen.textinput(title=f"{score}/{len(data_file)} States Correct", prompt="What's another state's name?").tolower()
#     another_answer = another_answer.lower()
    
# screen.exitonclick()