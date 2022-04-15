from turtle import Turtle, Screen
import pandas
turtle = Turtle()
screen = Screen()
screen.setup(width=650, height=500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

state_50 = []
while len(state_50) < 50:
    answer_state = screen.textinput(title=f"{len(state_50)}/50 States Correct", prompt="Guess the name of state.").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in state_50:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        state_50.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




