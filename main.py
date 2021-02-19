# hangman game tutorial
import pygame
import math

# Setup
pygame.init() 
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")
back_color = (255,255,255)
butt_color = (0,0,0)
LETTER_FONT = pygame.font.SysFont('times new roman', 42)

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


# Setup game loop
FPS = 60 #Defines the 'frame rate of game'
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(back_color)

    # Draw buttons
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, butt_color, (x,y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, (0,0,0))
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
    win.blit(images[hangman_status], (175,175))
    pygame.display.update()


while run:
    clock.tick(FPS) #game will runs at speed set above 
    draw()

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
                    print(ltr)


pygame.quit()
