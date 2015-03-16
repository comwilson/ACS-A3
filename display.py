import pygame

'''
SET UP PYGAME & GAME CONTROLLER
'''
def main():
	pygame.init()
	image = pygame.image.load("image4.jpg")
	window = pygame.display.set_mode((image.get_width(),image.get_height()))
	run = True
	while run:
		window.blit(image, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				run = False
		pygame.display.flip()
	pygame.quit()
	return

main()