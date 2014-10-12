import pygame
from TetrisGame import TetrisGame

if __name__=='__main__':
    start=True
    while(start):
        tetris=TetrisGame()
        score=tetris.main_loop()
        start=False
        while(not start):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    keys=pygame.key.get_pressed()
                    if(keys[pygame.K_y]):
                        start=True
                        pygame.mixer.music.stop()
                        break
                    if(keys[pygame.K_n]):
                        sys.exit()
            pygame.draw.rect(screen,WHITE,((0,90),(WIDTH,120)))
            font=pygame.font.SysFont("Lucida Console",24,True)
            text=font.render("Game Over!",1,BLACK)
            screen.blit(text,(10,100))
            font=pygame.font.SysFont("Lucida Console",16,True)
            text=font.render("Score: "+str(score),1,BLACK)
            screen.blit(text,(10,140))
            font=pygame.font.SysFont("Lucida Console",16,True)
            text=font.render("Continue? (y/n)",1,BLUE)
            screen.blit(text,(10,180))
            pygame.display.flip()

