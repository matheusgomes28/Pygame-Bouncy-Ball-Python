import pygame

pygame.init() 


def calculate_accel(forces, m):
	"""This function will calculate the acceleration
	of an object using newton's law: F = MA

	if mass = 1:
	calculate_accel([0,10]) -> [0,10] 
	"""

	temp = [0,0] # Temporary holder for resultant force

	for i in forces:
		temp[0] = temp[0] + i[0]
		temp[1] = temp[1] + i[1]

	return pygame.math.Vector2([round(temp[0] / m), round(temp[1] / m)])

def ball_collision(list_of_balls):
	""" This function returns True if a ball
	object collides with another ball object"""

	for a1 in list_of_balls:
		for a2 in list_of_balls:
			if (a1.center.distance_to(a2.center)) <=  (a1.RADIUS + a2.RADIUS):
				if a1.center != a2.center:
					return True
				else:
					return False
			else:
				return False

def handle_ground_collision(ball_obj, rec_obj):
	"""This function works as a collision detection for
	the ground and the ball. This is still a primitive 
	collision detector. 

	(all object, Rectangle object) -> Boolean"""

	temp = pygame.math.Vector2((ball_obj.center[0], ball_obj.center[1] + ball_obj.RADIUS))

	if temp.distance_to([ball_obj.center[0], rec_obj.center[1] - rec_obj.HEIGHT/2]) == 0:
		return True
	else: 
		return False