import turtle
from pythagoras_tree import draw_tree

def main():
    level = int(input("Введіть рівень рекурсії (наприклад 6): "))
    
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Фрактал: дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)   # Повертаємо вгору
    t.up()
    t.backward(200)
    t.down()

    draw_tree(t, 100, level)

    screen.mainloop()

if __name__ == "__main__":
    main()