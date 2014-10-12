class TetrisGame:
    ''' TetrisGame class controls the gameplay
        Attributes:
            game_still_on - type: bool - indicating whether the game is still on, or has been lost
                It starts of True. Toggle this to False to let the main loop to know that the game has ended
            speed - type: int - the rate of piece going down, 1 square per {speed} millisecond
            grid - type: 2D list of Square - the current state of the board
            crnt - type: Piece - the currently active Piece
    '''

    def __init__(self):
        # Initialize the game config
        self.game_still_on = True
        self.speed = 1000
        self.grid = []

        # Initialize the first Piece
        self.crnt = self.create_new_piece()

        # Schedule an event to be fired {speed} milliseconds from now
        # Or we should say, the 'moving down' tick
        pygame.time.set_timer(pygame.USEREVENT,self.speed) 

        # Start the game
        self.main_loop()

    def create_new_piece(self):
        ''' Create a random new Piece centered at the center top
            @Returns Piece
        '''

    def main_loop(self):
        ''' The main loop of the game.
            Two main things: 
                1. Responds to events and update game data
                2. Draw from game data
        '''

        while self.game_still_on:
            #read_events and update_data
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    self.handle_key_event(self.crnt)
                if self.paused: break
                if event.type==pygame.USEREVENT: 
                    # time for {crnt} to move down one square
                    self.one_tick()
            
            #draw_objects
            self.draw() 

    def handle_key_event(self):
        ''' Handle key events fired by player
        '''

        # Ask pygame, what keys are getting pressed
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_ESCAPE]): 
            sys.exit()
        if(keys[pygame.K_DOWN]):
            # Down key is pressed, tell the Piece to move down by one Square
            if(not self.crnt.move_down(self.grid)): 
                # The Piece cannot move down anymore. Settle it.
                self.settle_block()
        if(keys[pygame.K_LEFT]):
            self.crnt.move_left(self.grid)
        if(keys[pygame.K_RIGHT]):
            self.crnt.move_right(self.grid)
        if(keys[pygame.K_a]):
            self.crnt.rotate_CCW(self.grid)
        if(keys[pygame.K_d]):
            self.crnt.rotate_CW(self.grid)
    
    def settle_block(self):
        ''' The {crnt} Piece has reached an unpassable bottom
            We will 'settle' that Piece
        '''

        for square in self.crnt.squares:
            # Check every Square of the {crnt} Piece for losing condition
            # Or store them in {grid}
            if(square.is_invalid()):
                self.game_still_on=False
            else: 
                self.grid[square.y/SQUARE_SIZE][square.x/SQUARE_SIZE]=square
        
        if(not self.game_still_on): 
            return

        # Try to clear any full horizontal lines
        self.clear_lines()

        # Create new piece
        self.crnt=self.create_new_piece()

        # Schedule the next 'moving down' tick
        pygame.time.set_timer(pygame.USEREVENT,0)
        pygame.time.set_timer(pygame.USEREVENT,self.speed)

    def clear_lines(self):
        ''' Check {grid} for any full horizontal lines
            For each horizontal line, we should clear them, move all pieces above it down, and give the player some points
        '''

    def one_tick(self):
        ''' The {crnt} Piece should fall down by one Square. This will happen every {speed} milliseconds.
        '''

        # Tell the Piece to move down by one Square
        if(not self.crnt.move_down(self.grid)): 
            # The Piece cannot move down anymore. Settle it.
            self.settle_block()

class Piece:
    ''' Piece represents a Tetris piece
        Attributes:
            type - type: int - an enum indicating which kind of piece this Piece is. e.g.
                0:I, 1:J, 2:L, 3:O, 4:S, 5:T, 6:Z
            color - type: tuple of 3 ints - indicating the RGB color of the piece
            y - type: int - indicating the vertical position of the center of this piece in the grid (0..20)
            x - type: int - indicating the horizontal position of the center of this piece in the grid (0..10)
            squares - type: list of Square - the Squares this piece is constructed of
    '''

    def __init__(self,type):
        ''' Initialize color, y, x, and squares for corresponding {type}
            Please refer to PDF guideline for how you should position the Square(s)
            @Param type - type: int - see the type description on the class level above
        '''

    def move_down(self,grid):
        ''' Attempt to move this Piece by one unit down
            @Param grid - 2D list of Square - the current board state
            @Returns bool - returns False if the Piece cannot move down further
        '''

    def move_left(self,grid):
        ''' Attempt to move this Piece by one unit left
            @Param grid - 2D list of Square - the current board state
        '''

    def move_right(self,grid):
        ''' Attempt to move this Piece by one unit right
            @Param grid - 2D list of Square - the current board state
        '''
    
    def rotate_CW(self,grid):
        ''' Attempt to rotate this Piece by 90 degree clockwise
            @Param grid - 2D list of Square - the current board state
        '''

    def rotate_CCW(self,grid):
        ''' Attempt to rotate this Piece by 90 degree counter-clockwise
            @Param grid - 2D list of Square - the current board state
        '''

    def draw(self):
        for square in self.squares:
            square.draw()

Class Square:
    ''' Square represents a square block. A Piece is made of four Square(s)
        Attributes:
            color - type: tuple of 3 ints - indicating the RGB color of the Square
            y - type: int - indicating the vertical position of the center of this piece in the grid (0..20)
            x - type: int - indicating the horizontal position of the center of this piece in the grid (0..10)
    '''
    def __init__(self,color,pos):
        ''' Initialize color, y, and x of the Square
            @Param color - type: tuple of 3 ints - indicating the RGB color of the Square
            @Param pos - type: tuple of 2 ints - indicating the x and y position of the Square
        '''
    
    def move_up(self):

    def move_down(self):

    def move_left(self):

    def move_right(self):

    def rotate_CW(self):

    def rotate_CCW(self):
    
    def draw(self):

if __name__=='__main__':
    TetrisGame()