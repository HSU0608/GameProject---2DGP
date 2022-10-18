from pico2d import *

WIDTH, HEIGHT = 800, 600

def handle_events():
    # fill here
    global running
    global look
    global go
    global jump
    global y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                look = True
                go = True
            elif event.key == SDLK_RIGHT:
                look = False
                go = True
            elif event.key == SDLK_UP:
                if y <= 40:
                    jump = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                go = False
            elif event.key == SDLK_RIGHT:
                go = False

open_canvas(WIDTH, HEIGHT)
mario = load_image('mario3.png')
map = load_image('Bossmap.png')
grass = load_image('grass.png')
running = True
look = True
go = False
jump = False
x, y = WIDTH // 2, HEIGHT // 2
frame_x, frame_y = 0, 7
width, height = 64, 85
down_vector = 0
g = 10
hide_cursor()

while running:
    clear_canvas()
    if go:
        if look:
            x -= 5
        else:
            x += 5
        frame_x = (frame_x + 1) % 3

    else:
        frame_x = 0
    if y > 40:
        down_vector -= g
    if jump:
        down_vector = 40
        jump = False
    elif y <= 40:
        y = 40
        down_vector = 0
    y += down_vector
    map.draw(WIDTH // 2, HEIGHT // 2)
    grass.draw(400, -20)
    mario.clip_draw(frame_x * width + int((frame_x + 1) * 0.5), frame_y * height, width, height, x, y)
    update_canvas()
    delay(0.05)
    handle_events()

close_canvas()