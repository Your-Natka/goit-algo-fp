import turtle
import math

def draw_tree(t, branch_length, level):
    """Рекурсивне малювання дерева Піфагора"""
    if level == 0:
        return
    
    # Малюємо гілку
    t.forward(branch_length)

    # Ліва гілка
    t.left(45)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємось назад і малюємо праву
    t.right(90)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Відновлюємо положення
    t.left(45)
    t.backward(branch_length)