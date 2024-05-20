import turtle
import math

def draw_pythagoras_tree(length, level):
    """
    Функція для малювання фрактала "дерево Піфагора" за допомогою рекурсії.

    Параметри:
    - length: довжина початкової гілки
    - level: рівень рекурсії, глибина дерева
    """

    # Базовий випадок для рекурсії: якщо рівень 0, повернення
    if level == 0:
        return
    
    # Малюємо початкову гілку
    turtle.forward(length)

    # Поворот та рекурсивний виклик для лівої гілки
    turtle.left(45)
    draw_pythagoras_tree(length * (math.sqrt(2) / 2), level - 1) 

    # Поворот та рекурсивний виклик для правої гілки
    turtle.right(90)
    draw_pythagoras_tree(length * (math.sqrt(2) / 2), level - 1)

    # Повернення до початкового положення
    turtle.left(45)
    turtle.backward(length)

def main():
    # Запит користувача на введення рівня рекурсії
    level = int(input("Enter the level of recursion: "))

    # Налаштування швидкості малювання та орієнтація turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.color("green")

    # Виклик функції для малювання дерева
    draw_pythagoras_tree(100, level)

    # Виклик функції для завершення turtle
    turtle.done()

if __name__ == "__main__":
    main()
