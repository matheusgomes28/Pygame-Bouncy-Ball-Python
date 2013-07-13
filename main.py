import pygame, classes, sys
from pygame.locals import *
from functions import *

pygame.init() #Initialising pygame functions and variables


#Colors   R   G   B
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
BLUE  = (  0,  0,255)

FPS = 200 #Frames per second / display update time

#########################
### Movement settings ###
#########################

forces = [] # Empty forces list / holds forces acting on a particle / Forces in newtons
mass = 10 # Mass of the ball in kg.
g = 9.8 #universal gravity pull
ACCEL = pygame.math.Vector2((0, 0)) #Acceleration vector
velocity = pygame.math.Vector2([0,0]) #Velocity starting at 0
METRES = 200 # 200 pixels == 1 metres
friction = 3
is_vert_rest = False

def detect_collision(ball_center, rec_direction, rec_range):
	"""Advanced collision detection, uses vectors in order
	to triangulate positions and distances."""

	pass



def main():
	""" Main program precedure. This function contains
	the game loop."""

	global DISPLAY, FPSCLOCK, ball, rectangle  #Canvas globals created inside main function / only initializes if this is "__main__"
	global ACCEL, velocity, forces, is_vert_rest # Outside-created variables / Re-declaring so we can modify the values globally

	#  Display settings
	DISPLAY = pygame.display.set_mode((400,600))
	pygame.display.set_caption("Vector Test")

	ball = classes.Ball(DISPLAY, BLUE, (200, 200), 40)
	rectangle = classes.RecObstacle(DISPLAY, BLACK, (200,575), 400, 50)

	FPSCLOCK = pygame.time.Clock()

	
	while True:
		## Constant updates of the game ###
		DISPLAY.fill(WHITE)
		rectangle.draw()


		############################
		### Dynamics of the ball ###
		############################

		forces.append([0, mass * g]) # Acceleration due to gravity

		#Collision detection
		if handle_ground_collision(ball, rectangle):
			velocity[1] = -.8*(velocity[1])
			velocity[0] = velocity[0] * (1 - (friction / FPS))

			if velocity[1] < (1/FPS) and velocity[1] > -(1/FPS):  #Limit of movement
				is_vert_rest = True
			else:
				is_vert_rest = False

			ball.draw()

		#Velocity update
		velocity[1] = velocity[1] + (ACCEL[1] / FPS)
		
		if (ball.center[1] + ball.RADIUS) + (velocity[1] + (ACCEL[1] / FPS)) >= (rectangle.center[1] - (rectangle.HEIGHT / 2)):
			ball.move(velocity[0], (rectangle.center[1] - rectangle.HEIGHT/2) - (ball.center[1] + ball.RADIUS))
		else:
			ball.move((velocity[0] * METRES) / FPS, (velocity[1] * METRES) / FPS)
		############################


		if is_vert_rest:
			ACCEL[1] = 0
			velocity[1] = 0
		else:
			ACCEL = calculate_accel(forces, mass) # Calculate acceleration


		forces = []

		mouse = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		if mouse[0]:
			pygame.draw.aaline(DISPLAY, BLACK, mouse_pos, ball.center)

		# QUIT event checking
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP :
				velocity[0] = velocity[0] + (mouse_pos[0] - ball.center[0]) / (METRES / 4)
				velocity[1] = velocity[1] + (mouse_pos[1] - ball.center[1]) / (METRES / 4)



		pygame.display.update() # update the canvas
		FPSCLOCK.tick(FPS)
	

if __name__ == "__main__":
	main()



##################
# CODE BY: Matheus Gomes
# Open source
# Free to use and modify
##################