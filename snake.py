"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"""5 colores para elegir con el importado de random - choice"""
Colors = ['green', 'yellow', 'blue', 'purple', 'magenta']

colorSnake = choice(Colors)
colorFood = choice(Colors)
"""si se repite un color, buscar otro color de la lista"""
while(True):
    if(colorSnake == colorFood):
        colorFood = choice(Colors)
    else:
        break

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def moveFood():
    """Se escoge una dirección al azar para que la fruta se mueva"""
    options = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    step = choice(options)
    new = food + step
    if inside(new):
       food.move(step)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    """Se toma un número al azar hasta el 5 cada movimiento, y si es 0, se mueve la fruta dentro de la pantalla"""
    if randrange(5) == 0:
       moveFood()

    clear()
    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
