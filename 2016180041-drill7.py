from pico2d import *

import random


class Grass:
    def __init__(self):
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
        self.frame = random.randint(2, 7)

    def update(self):
        self.y -= self.frame
        if self.y < 60:
            self.y = 61

    def draw(self):
        self.image.draw(self.x, self.y)


class Balls:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
        self.frame = random.randint(2, 7)

    def update(self):
        self.y -= self.frame
        if self.y < 70:
            self.y = 71

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

boy = Boy()
ball = Ball()
balls = Balls()
grass = Grass()
team = [Boy() for i in range(11)]
temp1 = random.randint(1, 19)
temp2 = 20 - temp1
team2 = [Ball() for i in range(temp1)]
team3 = [Balls() for i in range(temp2)]

running = True


while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in team2:
        ball.update()
    for balls in team3:
        balls.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in team2:
        ball.draw()
    for balls in team3:
        balls.draw()
    update_canvas()

    delay(0.05)

close_canvas()
