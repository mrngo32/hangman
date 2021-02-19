# hangman game tutorial
import pygame
import os

# Setup display 
pygame.init() 
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")
color = (255,255,255)

# Load images
images = []
for i in range(7):
    image = pygame.image.load(r"C:\Users\Steven\Desktop\python_work\hangman\images\hangman" + str(i) + ".png")
    images.append(image)

# Game variable
hangman_status = 0


# Setup game loop
FPS = 60 #Defines the 'frame rate of game'
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) #game will runs at speed set above 

    win.fill(color)
    win.blit(images[hangman_status], (200,175))
    pygame.display.update()

    # Checks for any input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
