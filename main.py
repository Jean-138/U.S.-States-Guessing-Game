import turtle
import pandas as pd 

# I set up the screen and give it a title
screen = turtle.Screen()
screen.title("U.S States game")

# I add the blank map image to the turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

# I read the CSV file with all 50 states
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# I create an empty list to store the states I guessed correctly
guessed_states = []

# I keep asking for states until I have guessed all 50
while len(guessed_states) < 50:
    # I ask the user for another state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 states correct",
        prompt="What's another state's name?"
    ).title()

    # If I type Exit, I create a CSV file with the missing states
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states, columns=["states"])
        new_data.to_csv("states_to_learn.csv")
        break
    
    # If the answer is correct, I add the state and write its name on the map
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# keep the screen open until I click on it
screen.exitonclick()
