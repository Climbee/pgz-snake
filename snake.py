import random
import pgzrun

HT = 30
DIM = 40

OFFSET = 100

WIDTH = HT * (DIM + 1)
HEIGHT = HT * (DIM + 1) + OFFSET

top = 0
apple = (random.randint(0, DIM), random.randint(0, DIM))
snake = [(1,1)]
direction = (0,1)
counter = 0
gameover = False

def draw():
    global HT,top
    screen.clear()

    screen.draw.rect(Rect(0, 0, WIDTH, OFFSET - 1), (0,0,255))
    screen.draw.text(f"Your highest score: {top}", (400, 50), color="white")
    screen.draw.text("your length: " + str(len(snake)), (230, 50), color="white")

    if gameover:
        screen.draw.text("Game over!", (100, 50), color="white")
        return

    screen.draw.filled_rect(Rect(apple[0] * HT, apple[1] * HT + OFFSET, HT, HT), (255,0,0))
    for (x, y) in snake:
        screen.draw.filled_rect(Rect(x * HT, y * HT + OFFSET, HT, HT), (0, 255, 0))

def update():
    global direction, counter,gameover,snake,top

    if gameover and keyboard.space:
       gameover = False
       snake = [(1, 1)]
       direction = (0, 1)
       counter = 0
       return

    if keyboard.up and direction != (0, 1):
        direction = (0, -1)
    if keyboard.down and direction != (0, -1):
        direction = (0, 1)
    if keyboard.right and direction != (-1,0):
        direction = (1,0)
    if keyboard.left and direction != (1,0):
        direction = (-1,0)

    if len(snake) > top:
        top = len(snake)

    counter += 1
    if counter == 10:
        counter = 0
        move_snake()

def move_snake():
    global gameover
    head = snake[-1]
    newHead = (head[0] + direction[0], head[1] + direction[1])

    if newHead[0] < 0 or newHead[1] < 0 or newHead[0] > DIM or newHead[1] > DIM:
        gameover = True
    for segment in snake:
        if segment == newHead:
            gameover = True

    snake.append(newHead)

    if newHead != apple:
        del snake[0]
    else:
        generate_apple()

def generate_apple():
    global apple
    apple = (random.randint(0, DIM), random.randint(0, DIM))

pgzrun.go()