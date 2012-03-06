import os, sys
import pygame

HEIGHT,WIDTH=640,480

screen=pygame.display.set_mode((HEIGHT,WIDTH));
#surface set_mode(height,width,flag,color). Color will be automatically fitted if not supplied

class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Adhit's Tetris")
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

if __name__=='__main__':
    tetris=Tetris()
    tetris.main_loop()
