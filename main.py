# Refreshing my Memory
#devs

# New commit
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()
guesses = 0
valid_states = []

correct_answers = 0

while guesses < 50 and len(valid_states) < 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50", prompt="What's another state's name?").title()
    guesses += 1

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in valid_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_2_learn.csv")
        break

    if answer_state in states:
        valid_state = states_data[states_data["state"] == answer_state]
        valid_states.append(answer_state)
        correct_answers = len(valid_states)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(valid_state.x), int(valid_state.y))
        t.write(f"{answer_state}")


screen.exitonclick()
