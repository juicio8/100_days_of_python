import turtle

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# def get_coor(x, y):
#     print(x, y)
#
#
turtle.shape(image)
# turtle.onscreenclick(get_coor)

answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
turtle.mainloop()
# screen.exitonclick()
