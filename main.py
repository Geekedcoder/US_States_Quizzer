import turtle
import pandas

# Background
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Pandas - Reading CSV and lists
State_Data = pandas.read_csv("50_states.csv")
State = State_Data["state"]
correct_states = []
Score = 0

while len(correct_states) < 50:
    answer_the_state = screen.textinput(title=f"{Score}/50", prompt="Guess a state").title()
    State_Coor = State_Data[State_Data.state == answer_the_state]
    if answer_the_state == "Exit":
        missing_states = [state for state in State if state not in correct_states]
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        exit()
    for state in State:
        if state == answer_the_state:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(int(State_Coor.x), int(State_Coor.y))
            t.write(answer_the_state, align="center", font=("Arial", 12, "normal"))
            correct_states.append(answer_the_state)
            Score = len(correct_states)
