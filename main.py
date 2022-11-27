import pygame
import time
import os
import random

pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('Lemon\'s wacky chess game')
WIDTH, HEIGHT = 800, 800 
APP = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

hundred = 100
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BPAWN = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'bpawn.png')), (100, 100))
BKNIGHT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'bknight.png')), (100, 100))
BROOK = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'brook.png')), (100, 100))
BBISH = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'bbish.png')), (100, 100))
BQUEEN = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'bqueen.png')), (100, 100))
BKING = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'bking.png')), (100, 100))

WPAWN = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wpawn.png')), (100, 100))
WKNIGHT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wknight.png')), (100, 100))
WROOK = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wrook.png')), (100, 100))
WBISH = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wbish.png')), (100, 100))
WQUEEN = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wqueen.png')), (100, 100))
WKING = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Pieces', 'wking.png')), (100, 100))

class Pawn:
    def __init__(self, pawn_type, pawnx, pawny):
        self.pawn_img = None
        if pawn_type == 'black':
            self.pawn_img = BPAWN.convert()
        elif pawn_type == 'white':
            self.pawn_img = WPAWN.convert()
        self.pawn_rect = self.pawn_img.get_rect()
        self.pawn_rect.topleft = (pawnx, pawny)

    def move(self):
        self.pawn_rect = self.pawn_rect.move([0, 1])

pawns = []
coords = [[0, 100], [100, 100], [200, 100], [300, 100], [400, 100], [500, 100], [600, 100], [700, 100], [800, 100], [900, 100]]
for [x, y] in coords:
    pawn = Pawn('black', x, y)





CHESS_BOARD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Boards', 'tournament.png')), (WIDTH, HEIGHT))

def make_board(rows,width):
    grid = []
    gap = WIDTH // rows

def draw_window():
    APP.blit(CHESS_BOARD, (0,0))
    APP.blit(BPAWN, (0, 600))
    APP.blit(BPAWN, (100, 600))
    APP.blit(BPAWN, (200, 600))
    APP.blit(BPAWN, (300, 600))
    APP.blit(BPAWN, (400, 600))
    APP.blit(BPAWN, (500, 600))
    APP.blit(BPAWN, (600, 600))
    APP.blit(BPAWN, (700, 600))

    APP.blit(WPAWN, (0, 100))
    APP.blit(WPAWN, (100, 100))
    APP.blit(WPAWN, (200, 100))
    APP.blit(WPAWN, (300, 100))
    APP.blit(WPAWN, (400, 100))
    APP.blit(WPAWN, (500, 100))
    APP.blit(WPAWN, (600, 100))
    APP.blit(WPAWN, (700, 100))

    APP.blit(BROOK, (0, 700))
    APP.blit(BROOK, (700, 700))

    APP.blit(WROOK, (0, 0))
    APP.blit(WROOK, (700, 0))

    APP.blit(BKNIGHT, (100, 700))
    APP.blit(BKNIGHT, (600, 700))

    APP.blit(WKNIGHT, (100, 0))
    APP.blit(WKNIGHT, (600, 0))

    APP.blit(BBISH, (200, 700))
    APP.blit(BBISH, (500, 700))

    APP.blit(WBISH, (200, 0))
    APP.blit(WBISH, (500, 0))

    APP.blit(BQUEEN, (300, 700))

    APP.blit(WQUEEN, (300, 0))

    APP.blit(BKING, (400, 700))

    APP.blit(WKING, (400, 0))
    

    pygame.display.update()



# def handle_pawn(keys_pressed, pawn):
#     keys_pressed = pygame.key.get_pressed()
#     if keys_pressed[pygame.K_]
#         pawn.x -= VEL

# def handle_knight():

# def handle_rook():

# def handle_bish():

# def handle_queen():

# def handle_king():


def main():
    clock = pygame.time.Clock()
    run = True
    pawn1 = Pawn('white', 100, 100)
    pawn1.move()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == APP.MOUSEBUTTONDOWN:
                location = APP.mouse.get_pos() 
    


        draw_window()


if __name__ == '__main__':
    main()