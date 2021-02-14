import pygame
pygame.init()
gameWindow = pygame.display.set_mode((1200 , 500)) #creating game window
pygame.display.set_caption("notty snake")          #giving name to the game

#creating game specific variables:
exit_game = False
game_over = False

#creating game loop
while not exit_game:                              #loop for running game
    for event in pygame.event.get():              #get events
        if event.type == pygame.QUIT:             #close the game
            exit_game = True

        if event.type == pygame.KEYDOWN:          #check if key is press or not
            if event.key == pygame.K_RIGHT:       #check right arrow key is press or not
                print("you have pressed right arrow key")

pygame.quit()
quit()