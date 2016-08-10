
import arcade
import random
from math import sin, cos, floor, radians
from settings import *
from sprites import grid, cell_sprite

class Main_Window(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCR_W, SCR_H)
        self.max_pop = 5
        self.frame_count = 0
        self.all_sprites_list = None
        self.cell_list = None
        self.player_sprite = None
        self.view_left = 0
        self.view_bottom = 0
        arcade.set_background_color(arcade.color.BLACK)
        self.time_run = 0      
    def start_new_game(self):
        self.all_sprites_list = arcade.SpriteList()
        self.cell_list = arcade.SpriteList()
        self.player_sprite = cell_sprite(cell_sprite_path, SPRITE_SCALING)
        self.all_sprites_list.append(self.player_sprite)
    def on_draw(self):
        arcade.start_render()
        self.grid = grid(GRID_W,GRID_H,GRID_MARGIN,SIZE)
        self.grid.draw()
        self.all_sprites_list.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.close()
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 15
        if symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = -15
        if symbol == arcade.key.UP:
            self.player_sprite.thrust = 5  
        if symbol == arcade.key.DOWN:
            self.player_sprite.thrust = -5
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        elif symbol == arcade.key.UP:
            self.player_sprite.thrust = 0
        elif symbol == arcade.key.DOWN:
            self.player_sprite.thrust = 0
    def animate(self, x):
        self.all_sprites_list.update()
        is_changed = False
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            is_changed = True
        right_bndry = self.view_left + SCR_W - VIEWPORT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            is_changed = True
        top_bndry = self.view_bottom + SCR_H - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            is_changed = True
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            is_changed = True
        if is_changed:
            arcade.set_viewport(self.view_left,
                                SCR_W + self.view_left,
                                self.view_bottom,
                                SCR_H + self.view_bottom)
    def on_mouse_press(self,x,y,button,modifiers):
        col = x // (GRID_W + GRID_MARGIN)
        row = x // (GRID_H + GRID_MARGIN)
        print("Click coordinates: ({},{}). Grid coordinates: ({},{})"
              .format(x,y,row,col))
    def run():
        return arcade.run()

