# hangman game tutorial
import pygame
import math
import random

# Setup
pygame.init() 
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")
back_color = (255,255,255)
butt_color = (0,0,0)
LETTER_FONT = pygame.font.SysFont('times new roman', 42)
WORD_FONT = pygame.font.SysFont('comicsans', 64)
TITLE_FONT = pygame.font.SysFont('comicsans', 72)

# Load images
images = []
for i in range(7):
    image = pygame.image.load(r"C:\Users\Steven\Desktop\python_work\hangman\images\hangman" 
    + str(i) + ".png")
    images.append(image)

# Button variables
RADIUS = 28
GAP = 18
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 600
A = 65
for i in range(26):
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + ((i // 13) * (30 + RADIUS * 2))
    letters.append([x, y, chr(A + i)])

# Game variable
hangman_status = 0
with open("random.txt", "r") as file:
    allText = file.read()
    word_list = list(map(str, allText.split()))
word = random.choice(word_list).upper()
guessed =[]


# Setup game loop
FPS = 60 #Defines the 'frame rate of game'
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(back_color)
    text = TITLE_FONT.render("HANGMAN", 1, (0,0,0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
            
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, (0,0,0))
    win.blit(text, (500, 300))
        

    # Draw buttons
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, butt_color, (x,y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, (0,0,0))
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
    win.blit(images[hangman_status], (175,175))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(back_color)
    text = WORD_FONT.render(message, 1, (0,0,0))
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    
    clock.tick(FPS) #game will runs at speed set above 
   
    # Checks for any input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr = letter
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                if dis < RADIUS:
                    letters.pop(letters.index(letter))
                    guessed.append(ltr)
                    if ltr not in word:
                        hangman_status += 1
                        

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    
    if won:
        display_message("YOU WON!!!")
        break
    
    if hangman_status == 6:
        display_message("UH OH, YOU LOST!" + word)
        break

pygame.quit()
