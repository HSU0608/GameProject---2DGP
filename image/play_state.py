from pico2d import *
import game_framework
import logo_state
import math

g = 6
mario = None
running = None

class Mario:
    image = None
    def __init__(self, x = 500, y = 200, state = 0):
        if Mario.image == None:
            Mario.image = load_image('mario2.png')
        self.x, self.y = x, y
        self.direction = True
        self.go = False
        self.jump = False
        self.float = True
        self.old_y = 0
        self.spec = False
        self.frame_x, self.frame_y = 0, 7
        self.width, self.height = 64, 85
        self.velocity = 0
        self.floor = 25
        self.cap = 30
        self.adtime = 0
        self.status = state # 0 big mario 1 small mario
        if self.status == 0:
            self.frame_y = 7
            self.frame_x = 0
            self.floor = 25
            self.y += 20
            self.cap = 30
            self.status = 0
            self.float = True
            self.adtime = 5
        elif self.status == 1:
            self.frame_y = 9
            self.frame_x = 0
            self.floor = 8
            self.cap = 25
            self.status = 1
            self.float = True
            self.status = 1
        self.dead = False

def handle_events():
    def handle_events():
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(logo_state)
        running = False
def update(self):
    if self.go:
        if self.frame_x != 7:
            if self.direction:
                self.x -= 18
            else:
                self.x += 18

    if self.float == False:
        if self.frame_y == 7:
            if self.frame_x == 2:
                self.frame_y = 6
                self.frame_x = (self.frame_x + 1) % 3
            elif self.frame_y == 6:
                if self.frame_x == 2:
                    self.frame_y = 7
                    self.frame_x = (self.frame_x + 1) % 3
            elif self.frame_y == 9:
                if self.frame_x == 1:
                    self.frame_y = 8
                    self.frame_x = (self.frame_x + 1) % 2
            elif self.frame_y == 8:
                if self.frame_x == 1:
                    self.frame_y = 9
                    self.frame_x = (self.frame_x + 1) % 2
    else:
        if self.float == False:
            self.frame_x = 0
        if self.frame_y == 6 or self.frame_y == 8:
            self.frame_y = self.frame_y + 1

        if self.jump:
            self.velocity = 50
            if self.frame_y == 6 or self.frame_y == 8:
                self.frame_y = self.frame_y + 1
            self.frame_x = 3
            self.jump = False
            self.float = True
        if self.spec:
            self.velocity = -g
            self.spec = False
            if self.frame_y == 6 or self.frame_y == 8:
                self.frame_y = self.frame_y + 1
            self.frame_x = 7

        self.old_y = self.y

        if self.go:
            self.float = True

        if self.float:
            self.velocity -= g
            if self.frame_x == 7:
                self.velocity -= g
            if self.velocity < -30:
                self.velocity = -30
            self.y += self.velocity


        if self.adtime > 0:
            self.adtime -= 1

        if self.y < -100:
            self.dead = True

    def draw(self):
        if self.direction:
            Mario.clip_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, self.x, self.y)

def enter():
    global mario, running
    mario = Mario()
    running = True

def exit():
    global mario
    del mario

def draw():
    clear_canvas()
    mario.draw()
    update_canvas()


    return True
