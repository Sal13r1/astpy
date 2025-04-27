import pygame
from pygame.locals import *
from constants import *



def main():

	pygame.init()
	de_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	state = True

	while state:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0, 0, 0))
		pygame.display.flip()
		temp = de_clock.tick(60)
		dt = temp/1000

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}\n")

if __name__=="__main__":
	main()