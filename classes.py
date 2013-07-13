import pygame, sys
import pygame.gfxdraw
pygame.init()

class Obstacle(object):
	""" The Obstacle class defines simple methods and properties of 
		obstacle objects such as rectangles and circles"""

	def __init__(self, center, WIDTH, HEIGHT):
		self.center = pygame.math.Vector2(center)
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.top_left = [(self.center[0] - (WIDTH / 2)),(self.center[1] - (HEIGHT / 2))]

	def in_range(directions, width, height):
		"""This method returns True if the object is 
		inside the range of another object (NOT CIRCLE!!!)"""


class Ball(Obstacle):
	"""
	This class defines a ball object

	(surface, color, center, width/radius) -> GUI object.
	"""

	def __init__(self, SURFACE, COLOR, center, WIDTH):
		assert (type(center) == tuple), "Center must be a coordinate"
		Obstacle.__init__(self, center, WIDTH, WIDTH) # Width sent twice as the height = width.
		self.SURFACE = SURFACE
		self.COLOR = COLOR
		self.RADIUS = int(self.WIDTH / 2)
		
	def draw(self):
		#pygame.draw.circle(self.SURFACE, self.COLOR, (int(self.center[0]), int(self.center[1])), self.RADIUS, 2)
		pygame.gfxdraw.filled_circle(self.SURFACE, int(self.center[0]), int(self.center[1]), self.RADIUS, self.COLOR)
		pygame.gfxdraw.aacircle(self.SURFACE, int(self.center[0]), int(self.center[1]), self.RADIUS, self.COLOR)

	def move(self, valueX=0, valueY=0):

		#Reassigning center vector
		self.center[0] = ((self.center[0] + valueX) % 400)
		self.center[1] = (self.center[1] + valueY)

		self.draw()


class RecObstacle(Obstacle):
	"""
	The RecObstacle class creates a new rectangle instance and adds
	methods and properties that allow the created rectangle to be 
	added to the 'display surface'

	(surface, color, center, width, height) -> GUI object
	  [display obj, list, list, int, int]
	"""

	def __init__(self, SURFACE, COLOR, center, WIDTH, HEIGHT):
		Obstacle.__init__(self,(center[0], center[1]), WIDTH, HEIGHT)
		self.SURFACE = SURFACE
		self.COLOR = COLOR
		self.directions = [[0,1]]
	def draw(self):
		pygame.draw.rect(self.SURFACE, self.COLOR, (self.top_left[0], self.top_left[1], self.WIDTH, self.HEIGHT))