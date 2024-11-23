"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

"""

import turtle
import math

#  Функція для рекурсивного малювання дерева Піфагора
def draw_tree(t, branch_length, level, angle):
    """
        t (turtle.Turtle): Об'єкт turtle (черепашки) для малювання.
        branch_length (float): Довжина гілки на поточному рівні.
        level (int): Поточний рівень рекурсії.
        angle (float): Кут нахилу гілок.
    """
    if level == 0:
        return

    # Малювання стовбура
    t.forward(branch_length)

    # Ліва гілка
    t.left(angle)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)
    t.right(angle)

    # Права гілка
    t.right(angle)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)
    t.left(angle)

    # Повернення до початкової точки
    t.backward(branch_length)

def main():
    # Створення та налаштування черепашки
    screen = turtle.Screen()
    screen.setup(800, 800)  # Встановлюємо розмір вікна
    screen.title("Дерево Піфагора")
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))
    angle = 45

    # Малювання дерева
    draw_tree(t, 100, level, angle)

    # Сховати черепашку
    t.hideturtle()

    # Зберегти зображення
    canvas = screen.getcanvas()
    canvas.postscript(file="images/pythagoras-tree.eps")
    
    try:
        from PIL import Image, EpsImagePlugin
        img = Image.open("images/pythagoras-tree.eps")
        img.save("images/pythagoras-tree.png", "png")
    except Exception as e:
        print(f"Помилка при конвертації в PNG: {e}")
        print("EPS файл збережено")

    screen.mainloop()

if __name__ == "__main__":
    main()