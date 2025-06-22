import pygame
from game import Game
from user import User

cardsUser1 = [
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Schirru.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Barclay Els.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Toruviel.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Recruit.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Veteran 1.png"
]

cardsUser2 = [
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Toruviel.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Recruit.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Veteran 1.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Veteran 2.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Yaevinn.png"
]



pygame.init()

screen = pygame.display.set_mode((1380, 870))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\board_optimized.png").convert_alpha()
bg = pygame.transform.scale(bg, (1080, 700))
user1 = User("Rolando", 0, [], None)
user2 = User("Elena", 0, [], None)
game = Game(user1, user2, 0, 0)
game.startGame(cardsUser1, cardsUser2)
#print("User 1: ", user1, "User 2: ", user2)

user1_cards = pygame.sprite.Group()
#print("USER1 Deck CARDSSS: ", user1.deckCards)
user1_cards.add(user1.deckCards)

user2_cards = pygame.sprite.Group()
user2_cards.add(user2.deckCards)
#print(user1_cards)
y_start = 50        # Starting Y position
y_spacing = 150     # Vertical space between cards

while running:
    # For loop to manage quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #This helped me to add a background image
    screen.blit(bg, (110, 110))
    #user1_cards.draw(screen)
    for index, card in enumerate(user1_cards):
        x = 10
        y = y_start + index * y_spacing  # Y increases with each card
        card.draw(screen, x, y)

    for index, card in enumerate(user2_cards):
        x = 1200
        y = y_start + index * y_spacing
        card.draw(screen, x, y)

    pygame.display.flip()
    

    # To-Do: Add Icon
    pygame.display.set_caption("My Gwent Game")

    
    #FPS
    clock.tick(60)

pygame.quit()