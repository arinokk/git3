import pygame

x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
clock = pygame.time.Clock()
pygame.init()

fps = 60
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption('image', 'Show Text')

font = pygame.font.Font('freesansbold.ttf', 100)
imp = pygame.image.load("img1.jpg").convert()
screen.blit(imp, (0, 0))
black = (0, 0, 0)
text = font.render(f'{x+y}', True, black)

textRect = text.get_rect()


while True:
    screen.blit(text, (50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(fps)
