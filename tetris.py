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

#pygame things
clock=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT));

class Square():
    def __init__(self,color,pos):
        self.color=color
        self.x=pos[0]
        self.y=pos[1]
    def move_up(self):
        self.y=self.y-FULL_WIDTH
    def move_down(self):
        self.y=self.y+FULL_WIDTH
    def move_left(self):
        self.x=self.x-FULL_WIDTH
    def move_right(self):
        self.x=self.x+FULL_WIDTH
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

class Block():
    def __init__(self,type):
        self.type=type
        self.squares=[]
        if(type==0): #4 squares vertical
            self.color=RED
            self.y=3*-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x,self.y-2*FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y+FULL_WIDTH)))
        elif(type==1): #T
            self.color=ORANGE
            self.y=-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
        elif(type==2): #square squares
            self.color=YELLOW
            self.y=-FULL_WIDTH
            self.x=240
            self.squares.append(Square(self.color,(self.x-HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+HALF_WIDTH,self.y+HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x-HALF_WIDTH,self.y+HALF_WIDTH)))
        elif(type==3): #inversed z
            self.color=GREEN
            self.y=-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y-FULL_WIDTH)))
        elif(type==4): #z
            self.color=BLUE
            self.y=-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y-FULL_WIDTH)))
        elif(type==5): #inversed L
            self.color=CYAN
            self.y=-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y-FULL_WIDTH)))
        elif(type==6): #L
            self.color=PURPLE
            self.y=-HALF_WIDTH
            self.x=220
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y-FULL_WIDTH)))
    def move_up(self):
        self.y-=FULL_WIDTH
        for square in self.squares:
            square.move_up()
    def move_down(self):
        self.y+=FULL_WIDTH
        for square in self.squares:
            square.move_down()
    def move_left(self):
        self.x-=FULL_WIDTH
        for square in self.squares:
            square.move_left()
    def move_right(self):
        self.x+=FULL_WIDTH
        for square in self.squares:
            square.move_right()
    def draw(self):
        for square in self.squares:
            square.draw()
    
class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Adhit's Tetris")
        self.test_block=Block(6)
    def handle_key_event(self,block):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            block.move_up()
        if keys[pygame.K_DOWN]:
            block.move_down()
        if keys[pygame.K_LEFT]:
            block.move_left()
        if keys[pygame.K_RIGHT]:
            block.move_right()
    def draw(self,block):
        screen.fill(BG_COLOR)
        block.draw()
        pygame.display.flip()
    def main_loop(self):
        pygame.key.set_repeat(50,20)
        while True: #game loop: read_events->update_data->draw_objects
            clock.tick(1000) #iterations in one second
            #read_events and update_data
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    self.handle_key_event(self.test_block)
            #draw_objects
            self.draw(self.test_block) 
if __name__=='__main__':
    tetris=Tetris()
    tetris.main_loop()
