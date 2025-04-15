import colorgram
import random
import turtle as t

#set color
# colors = colorgram.extract('download.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()
ts = tim.getscreen()
width = ts.window_width()
height = ts.window_height()
start_x = -width/2 + 50
tim.teleport(start_x, -height/2 +50)

color_list = [(225, 233, 238), (235, 37, 113), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50), (33, 122, 186), (52, 189, 227), (173, 44, 94), (242, 219, 57), (80, 24, 74), (127, 190, 92), (250, 2, 94), (242, 219, 57), (80, 24, 74), (127, 190, 92), (250, 223, 0), (23, 169, 122), (189, 67, 41), (207, 133, 165)]
dot_x = 0
dot_y = 0
while dot_y < 11:
    while dot_x < 11:
        tim.dot(20, random.choice(color_list))
        tim.teleport(tim.pos()[0] + 50)
        dot_x += 1
    tim.teleport(start_x, tim.pos()[1] + 50)
    dot_x = 0
    dot_y += 1

screen = t.Screen()
screen.exitonclick()