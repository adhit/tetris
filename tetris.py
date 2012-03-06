import os,sys
import pygame

#define colors
RED=255,0,64
ORANGE=255,64,0
YELLOW=191,255,0
GREEN=64,255,0
BLUE=0,64,255
CYAN=0,255,191
PURPLE=191,0,255
PINK=255,0,191
WHITE=255,255,255
BLACK=0,0,0
BG_COLOR=204,255,255
LINE_COLOR=BLACK

#define measures
HEIGHT,WIDTH=640,480
HALF_WIDTH=20
FULL_WIDTH=2*HALF_WIDTH
LINE_WIDTH=3

screen=pygame.display.set_mode((WIDTH,HEIGHT));
#surface set_mode(height,width,flag,color). Color will be automatically fitted if not supplied

class Square:
    def __init__(self,color,pos):
        self.color=color
        self.x=pos[0]
        self.y=pos[1]
    def draw(self):
        corners=[]
        corners.append((self.x-HALF_WIDTH,self.y-HALF_WIDTH))
        corners.append((self.x+HALF_WIDTH,self.y-HALF_WIDTH))
        corners.append((self.x+HALF_WIDTH,self.y+HALF_WIDTH))
        corners.append((self.x-HALF_WIDTH,self.y+HALF_WIDTH))
        screen.lock()
        pygame.draw.rect(screen,self.color,pygame.Rect((self.x-HALF_WIDTH,self.y-HALF_WIDTH),(FULL_WIDTH,FULL_WIDTH)))
        pygame.draw.lines(screen,LINE_COLOR,True,corners,LINE_WIDTH)
        screen.unlock()

class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Adhit's Tetris")
        self.test_square=Square(RED,(40,40))
    def draw(self,square):
        screen.fill(BG_COLOR)
        square.draw()
        pygame.display.flip()
    def main_loop(self):
        while True: #game loop: read_events->update_data->draw_objects
            #read_events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            #update_data:not yet
            #draw_objects
            self.draw(self.test_square)            

if __name__=='__main__':
    tetris=Tetris()
    tetris.main_loop()
