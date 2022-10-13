import pico2d
import game_framework

import logo_state
import play_state
import title_state

pico2d.open_canvas(800, 600)
game_framework.run(title_state)
game_framework.run(play_state)
game_framework.run(logo_state)

pico2d.close_canvas()