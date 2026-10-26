import turtle

window = turtle.Screen()
window.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# тут надо поменять цвет
colors = ["red", "purple", "blue", "green", "yellow", "orange"]

for x in range(300):
  t.pencolor(colors[x % 6])
  t.forward(x)
  t.left(59)

window.mainloop()

