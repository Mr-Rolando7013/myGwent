import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\board_optimized.png")

while running:
    # For loop to manage quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #This helped me to add a background image
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    # To-Do: Add Icon
    pygame.display.set_caption("My Gwent Game")
    
    #FPS
    clock.tick(60)

pygame.quit()