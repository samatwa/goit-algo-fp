import turtle
import math

def draw_pythagoras_tree(length, level):
    if level == 0:
        return
    
    turtle.forward(length)

    turtle.left(45)
    draw_pythagoras_tree(length *(math.sqrt(2) / 2), level - 1) 

    turtle.right(90)
    draw_pythagoras_tree(length *(math.sqrt(2) / 2), level - 1)

    turtle.left(45)
    turtle.backward(length)

def main():
    level = int(input("Enter the level of the tree: "))

    turtle.speed("fastest")
    turtle.left(90)

    draw_pythagoras_tree(100, level)

    turtle.done()

if __name__ == "__main__":
    main()