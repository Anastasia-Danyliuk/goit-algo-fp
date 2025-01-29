import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.right(90)
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.left(45)
    t.backward(length)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()

    draw_pythagoras_tree(t, 200, level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
