from arcade.color import *
from settings import SCR_W, SCR_H
from arcade import draw_rectangle_filled, draw_ellipse_filled, create_rectangle,render_rectangle_filled, Sprite
from math import sin, cos, radians
from util import Shape_Grid, Shape_Cell
class grid():
	def __init__(self, GRID_W: int = 0, GRID_H:int = 0, GRID_MARGIN:int = 1,SIZE:int = 0):
		self.GRID_W = GRID_W
		self.GRID_H = GRID_H
		self.GRID_MARGIN = GRID_MARGIN
		self.SIZE = SIZE
		self.GRID = []
		self.SHAPE_LIST = []
		for row in range(20):
			self.GRID.append([])
			for col in range(20):
				self.GRID[row].append([])
				x = (self.GRID_MARGIN + self.GRID_W ) * col + self.GRID_MARGIN + self.GRID_W //2
				y = (self.GRID_MARGIN + self.GRID_H ) * row + self.GRID_MARGIN + self.GRID_H //2
				self.SHAPE_LIST.append(create_rectangle(self.GRID_W,self.GRID_H,GREEN))
	def draw(self):
		for row in range(self.SIZE):
			for col in range(self.SIZE):
				x = (self.GRID_MARGIN + self.GRID_W ) * col + self.GRID_MARGIN + self.GRID_W //2
				y = (self.GRID_MARGIN + self.GRID_H ) * row + self.GRID_MARGIN + self.GRID_H //2
		for i in range(len(self.SHAPE_LIST)):
			render_rectangle_filled(self.SHAPE_LIST[i],x,y,(255,255,255))
		
#class cell():
	#def __init__(self, center_x: float=0, center_y: float=0, radius: float=5,angle: float=90):
		#self.center_x = center_x
		#self.center_y = center_y
		#self.radius = radius
		#self.angle = angle
	#def draw(self):
		#draw_ellipse_filled(self.center_x, self.center_y, self.radius, self.radius, (0,244,50), self.angle)
		#draw_rectangle_filled(self.center_x,self.center_y,self.center_x + self.radius, self.center_y + self.radius, (0,0,0),self.angle)
class cell_sprite(Sprite):
    def __init__(self,cell_sprite_path,SPRITE_SCALING):
        super().__init__(cell_sprite_path,SPRITE_SCALING)
        self.thrust = 0
        self.speed = 0
        self.max_speed=10
        self.drag = 1.5
        self.respawn()
        self.ID = "TESTING_CELL"
    def respawn(self):
        self.center_x = SCR_W/2
        self.center_y = SCR_H/2
        self.angle = 90
    def update(self):
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0
        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0
        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed
        self.change_x = -sin(radians(self.angle))*self.speed
        self.change_y = cos(radians(self.angle))*self.speed
        self.center_x += self.change_x
        self.center_y += self.change_y
        super().update()
    def getID(self):
        return self.ID	
