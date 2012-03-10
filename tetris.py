import os,sys
import pygame
import random
import math

#define colors
RED=255,0,64
ORANGE=255,64,0
YELLOW=191,255,0
GREEN=64,255,0
BLUE=0,64,255
CYAN=0,255,255
PURPLE=191,0,255
PINK=255,0,191
WHITE=255,255,255
BLACK=0,0,0
BG_COLOR=204,255,255
LINE_COLOR=BLACK

#define measures
HEIGHT,WIDTH=400,200
HALF_WIDTH=10
FULL_WIDTH=2*HALF_WIDTH
LINE_WIDTH=2
MID_X=WIDTH/2

#pygame things
clock=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT));

#timing things
last_move=0
last_rotate=0

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
    def rotate_CW(self):
        temp=self.x
        self.x=-self.y
        self.y=temp
    def rotate_CCW(self):
        temp=self.x
        self.x=self.y
        self.y=-temp
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
#type=0
        self.type=type
        self.squares=[]
        if(type==0): #4 squares vertical
            self.color=CYAN
            self.y=0
            self.x=MID_X
            self.squares.append(Square(self.color,(self.x-3*HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x-HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+3*HALF_WIDTH,self.y-HALF_WIDTH)))
        elif(type==1): #T
            self.color=PURPLE
            self.y=-HALF_WIDTH
            self.x=3*HALF_WIDTH
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
        elif(type==2): #square squares
            self.color=YELLOW
            self.y=-FULL_WIDTH
            self.x=MID_X
            self.squares.append(Square(self.color,(self.x-HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+HALF_WIDTH,self.y-HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x+HALF_WIDTH,self.y+HALF_WIDTH)))
            self.squares.append(Square(self.color,(self.x-HALF_WIDTH,self.y+HALF_WIDTH)))
        elif(type==3): #inversed z
            self.color=GREEN
            self.y=-HALF_WIDTH
            self.x=3*HALF_WIDTH
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y-FULL_WIDTH)))
        elif(type==4): #z
            self.color=RED
            self.y=-HALF_WIDTH
            self.x=3*HALF_WIDTH
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y-FULL_WIDTH)))
        elif(type==5): #inversed L
            self.color=BLUE
            self.y=-HALF_WIDTH
            self.x=3*HALF_WIDTH
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y-FULL_WIDTH)))
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
        elif(type==6): #L
            self.color=ORANGE
            self.y=-HALF_WIDTH
            self.x=3*HALF_WIDTH
            self.squares.append(Square(self.color,(self.x-FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y)))
            self.squares.append(Square(self.color,(self.x+FULL_WIDTH,self.y-FULL_WIDTH)))
    def move_up(self,grid):
        if(not self.can_move(0,-1,grid)): return
        self.y-=FULL_WIDTH
        for square in self.squares:
            square.move_up()
    def move_down(self,grid):
        if(not self.can_move(0,1,grid)): return False
        self.y+=FULL_WIDTH
        for square in self.squares:
            square.move_down()
        return True
    def move_left(self,grid):
        if(not self.can_move(-1,0,grid)): return
        self.x-=FULL_WIDTH
        for square in self.squares:
            square.move_left()
    def move_right(self,grid):
        if(not self.can_move(1,0,grid)): return
        self.x+=FULL_WIDTH
        for square in self.squares:
            square.move_right()
    def draw(self):
        for square in self.squares:
            square.draw()
    def rotate_CW(self,grid):
        if(not self.can_CW(grid)):
            return
        for square in self.squares:
            square.x-=self.x
            square.y-=self.y
            square.rotate_CW()
            square.x+=self.x
            square.y+=self.y
    def rotate_CCW(self,grid):
        if(not self.can_CCW(grid)): return
        for square in self.squares:
            square.x-=self.x
            square.y-=self.y
            square.rotate_CCW()
            square.x+=self.x
            square.y+=self.y
    def can_move(self,dx,dy,grid):
        for square in self.squares:
            x=(square.x/FULL_WIDTH)+dx
            y=(square.y/FULL_WIDTH)+dy
            if(y>=20 or x<0 or x>=10 or (y>=0 and grid[y][x] is not None)):
                return False
        return True
    def can_CW(self,grid):
        for square in self.squares:
            x=square.x-self.x
            y=square.y-self.y
            temp=x
            x=-y
            y=temp
            x=(x+self.x)/FULL_WIDTH
            y=(y+self.y)/FULL_WIDTH
            if(y>=20 or x<0 or x>=10 or (y>=0 and grid[y][x] is not None)): return False
        return True
    def can_CCW(self,grid):
        for square in self.squares:
            x=square.x-self.x
            y=square.y-self.y
            temp=x
            x=y
            y=-temp
            x=(x+self.x)/FULL_WIDTH
            y=(y+self.y)/FULL_WIDTH
            if(y>=20 or x<0 or x>=10 or (y>=0 and grid[y][x] is not None)): return False
        return True
            

class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Adhit's Tetris")
        self.speed=2000
        self.level=0
        self.cleared=0
        self.required=5
        self.speed_mult=0.8
        self.score_guide=[40,100,300,1200]
        self.score=0
        self.grid=[]
        for i in range(20):
            self.grid.append([])
            for j in range(10):
                self.grid[i].append(None)
    def handle_key_event(self,block):
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_UP]):
            block.move_up(self.grid)
        if(keys[pygame.K_DOWN]):
            if(not block.move_down(self.grid)): self.settle_block()
        if(keys[pygame.K_LEFT]):
            block.move_left(self.grid)
        if(keys[pygame.K_RIGHT]):
            block.move_right(self.grid)
        if(keys[pygame.K_a]):
            block.rotate_CCW(self.grid)
        if(keys[pygame.K_d]):
            block.rotate_CW(self.grid)
        if(keys[pygame.K_s]):
            self.debug()
    def debug(self):
        for i in range(20):
            s=""
            for j in range(10):
                if(self.grid[i][j] is None): s=s+"0"
                else: s=s+"1"
            print s
    def draw(self):
        screen.fill(BG_COLOR)
        self.crnt.draw()
        for i in range(20):
            for j in range(10):
                if(self.grid[i][j] is not None): self.grid[i][j].draw()
        pygame.display.flip()
    def custom_tick(self):
        #pygame.time.set_timer(pygame.USEREVENT,0)
        if(not self.crnt.move_down(self.grid)): self.settle_block()
    def clear_lines(self):
        count=0
        for i in range(20):
            full=True
            for j in range(10):
                if(self.grid[i][j] is None): 
                    full=False
                    break
            if(full):
                count+=1
                for j in range(10):
                    self.grid[i][j]=None
        i=19
        j=18
        while(i>0 and j>=0):
            null=True
            for k in range(10):
                if(self.grid[i][k] is not None):
                    null=False
                    break
            if(null):
                j=min(i-1,j)
                while(j>=0 and null):
                    null=True
                    for k in range(10):
                        if(self.grid[j][k] is not None):
                            null=False
                            break
                    if(null): j-=1
                if(j<0): break
                for k in range(10):
                    self.grid[i][k]=self.grid[j][k]
                    self.grid[j][k]=None
                    if(self.grid[i][k] is not None): self.grid[i][k].y=HALF_WIDTH+i*FULL_WIDTH
                j-=1
            i-=1
        if(count>0):
            self.score+=self.score_guide[count-1]*(self.level+1)
        self.cleared+=count
        if(self.cleared>=self.required):
            self.level+=1
            self.speed=int(math.ceil(self.speed_mult*self.speed))
            self.cleared-=self.required
            self.required=int(math.ceil(self.required/self.speed_mult))
        print "Score: "+str(self.score)
    def settle_block(self):
        if(not self.first_settle): return
#print "Settling"
#print str(self.crnt.x)+" "+str(self.crnt.y)
        self.first_settle=False
        for square in self.crnt.squares:
            self.grid[square.y/FULL_WIDTH][square.x/FULL_WIDTH]=square
        self.clear_lines()
        self.crnt=Block(random.randint(0,6))
        pygame.time.set_timer(pygame.USEREVENT,0)
        pygame.time.set_timer(pygame.USEREVENT,self.speed)
    def main_loop(self):
        pygame.key.set_repeat(200,50)
        self.crnt=Block(random.randint(0,6))
        pygame.time.set_timer(pygame.USEREVENT,self.speed) #this is the 'moving down' tick
        while True: #game loop: read_events->update_data->draw_objects
            #read_events and update_data
            self.first_settle=True
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    self.handle_key_event(self.crnt)
                if event.type==pygame.USEREVENT: #time for block to move down one square
                    self.custom_tick()
            #draw_objects
            self.draw() 
if __name__=='__main__':
    tetris=Tetris()
    tetris.main_loop()
