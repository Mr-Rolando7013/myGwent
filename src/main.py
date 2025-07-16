import pygame
from game import Game
from user import User
from getSwordAndBow import sword_or_bow

cardsUser1 = [
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Schirru.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Barclay Els.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Toruviel.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Recruit.png",
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Vrihedd Brigade Veteran 1.png"
]

cardsUser2 = [
    "C:\\Users\\byL0r3t\\Desktop\\pythonProjects\\myGwent\\assets\\images\\Scoia'tel\\Schirru.png",
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
bg = pygame.transform.scale(bg, (1080, 900))
user1 = User("Rolando", 0, [], None)
user2 = User("Elena", 0, [], None)
game = Game(user1, user2, 0, 0, True, False)
game.startGame(cardsUser1, cardsUser2)

user1_cards = list(user1.deckCards)
user2_cards = list(user2.deckCards)
user1_battlefieldCards = []
user2_battlefieldCards = []
y_start = 50        # Starting Y position
y_spacing = 150     # Vertical space between cards

sword_y = 315
sword_x_start = 460
sword_index = 0

bow_y = 170
bow_x_start = 460
bow_index = 0

range_y = 25
range_x_start = 460
range_index = 0

sword_y2 = 470
sword_x2_start = 460
sword_index2 = 0

bow_y2 = 610
bow_x2_start = 460
bow_index2 = 0

range_y2 = 750
range_x2_start = 460
range_index2 = 0

font = pygame.font.Font(None, 30)

points_rect_x = 200
points_rect_y = 200
points_width = 60
points_height = 30
value1 = 0

points2_rect_x = 300
points2_rect_y = 200
points2_width = 60
points2_height = 30
value2 = 0

for index, card in enumerate(user1_cards):
    card.rect.topleft = (10, y_start + index * y_spacing)

for index, card in enumerate(user2_cards):
    card.rect.topleft = (1200, y_start + index * y_spacing)

while running:
    
    # For loop to manage quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.isUser1Turn == True:
                for card in user1_cards:
                    print(f"User 1's turn: {game.isUser1Turn}, User 2's turn: {game.isUser2Turn}")
                    if card in user1_cards and card.rect.collidepoint(event.pos):
                        if not card.on_board:
                            card.on_board = True
                            user1_cards.remove(card)
                            user1_battlefieldCards.append(card)
                            # Move to battlefield position
                            if card.field == "bow":
                                card.rect.topleft = (bow_x_start + bow_index * 110, bow_y)
                                bow_index += 1
                                    
                            elif card.field == "sword":
                                # Move to battlefield position 
                                card.rect.topleft = (sword_x_start + sword_index * 110, sword_y)
                                sword_index += 1
                                    
                            elif card.field == "range":
                                # Move to siege position
                                card.rect.topleft = (range_x_start + range_index * 110, range_y)
                                range_index += 1
                                
                            elif card.field == "sword and bow":
                                answer = sword_or_bow()
                                print("Answer:", answer)
                                if answer == "sword":
                                    card.rect.topleft = (sword_x_start + sword_index * 110, sword_y)
                                    sword_index += 1
                                elif answer == "bow":
                                    card.rect.topleft = (bow_x_start + bow_index * 110, bow_y)
                                    bow_index += 1
                                else:
                                    print("Invalid choice. Card not placed.")
                            #The rounds system still has some bugs, but it works for now
                            game.isUser1Turn = False
                            game.isUser2Turn = True
                            value1 += card.damage
                            break
                        break
                
            elif game.isUser2Turn == True:
                for card in user2_cards:
                    if game.isUser2Turn == True:
                        print(f"User 1's turn: {game.isUser1Turn}, User 2's turn: {game.isUser2Turn}")
                        # Check if the card is in user2's hand and if it collides with the mouse click
                        if card in user2_cards and card.rect.collidepoint(event.pos):
                            if not card.on_board:
                                user2_cards.remove(card)
                                user2_battlefieldCards.append(card)
                                card.on_board = True
                                # Move to battlefield position
                                if card.field == "bow":
                                    card.rect.topleft = (bow_x2_start + bow_index2 * 110, bow_y2)
                                    bow_index2 += 1
                                elif card.field == "sword":
                                    # Move to battlefield position 
                                    card.rect.topleft = (sword_x2_start + sword_index2 * 110, sword_y2)
                                    sword_index2 += 1
                                elif card.field == "range":
                                    print("Range card placed in siege position.")
                                    # Move to siege position
                                    card.rect.topleft = (range_x2_start + range_index2 * 110, range_y2)
                                    range_index2 += 1

                                elif card.field == "sword and bow":
                                    answer = sword_or_bow()
                                    print("Answer:", answer)
                                    if answer == "sword":
                                        card.rect.topleft = (sword_x2_start + sword_index2 * 110, sword_y2)
                                        sword_index2 += 1
                                    elif answer == "bow":
                                        card.rect.topleft = (bow_x2_start + bow_index2 * 110, bow_y2)
                                        bow_index2 += 1
                                    else:
                                        print("Invalid choice. Card not placed.")
                                game.isUser2Turn = False
                                game.isUser1Turn = True
                                value2 += card.damage
                                break
                            break
    
    #This helped me to add a background image
    screen.fill((0,0,0))
    screen.blit(bg, (110, 0))

    pygame.draw.rect(screen, (255, 255, 255), (points_rect_x, points_rect_y, points_width, points_height))
    pygame.draw.rect(screen, (255, 255, 255), (points2_rect_x, points2_rect_y, points2_width, points2_height))

    text = font.render(str(value1), True, (0, 0, 0))
    text_rect = text.get_rect(center=(points_rect_x + points_width // 2, points_rect_y + points_height // 2))

    text2 = font.render(str(value2), True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(points2_rect_x + points2_width // 2, points2_rect_y + points2_height // 2))
    screen.blit(text2, text_rect2)
    screen.blit(text, text_rect)

    for card in user1_cards:
        screen.blit(card.image, card.rect)
    
    for card in user1_battlefieldCards:
        screen.blit(card.image, card.rect)

    for card in user2_cards:
        screen.blit(card.image, card.rect)

    for card in user2_battlefieldCards:
        screen.blit(card.image, card.rect)

    if len(user1_cards) == 0 and len(user2_cards) == 0:
        if value1 > value2:
            user1.gamesWon += 1
            print("User 1 wins!")
            running = False
        elif value2 > value1:
            user2.gamesWon += 1
            print("User 2 wins!")
            running = False
        else:
            print("It's a tie!")
            running = False

    #pygame.display.update()
    pygame.display.flip()
    

    # To-Do: Add Icon
    pygame.display.set_caption("My Gwent Game")

    
    #FPS
    clock.tick(60)

pygame.quit()