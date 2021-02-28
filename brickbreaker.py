# Jesus Robles
# 1/13/2021
# brickbreaker.py

# This program will simulate the game brick breaker in a graphics window 
# This program utilizes graphics.py open-source software written by John Zelle

# The last four functions in this file should be read first to understand how program works

from graphics import *

# These list of strings are converted to Text objects to be displayed in window
INSTRUCTIONS = ["Welcome to BrickBreaker!",
                "Instructions: ",
                "Use the 9 and 0 key to keep the ball from touching the bottom",
                "Break all the bricks before losing all three times",
                "Press any key to start playing the game. Goodluck!"]

PAUSE = ["The game is paused.",
         "Press any key to continue playing."]

VICTORY = ["Congratulations!",
           "You broke all the bricks!!",
           "Thank you for playing :)",
           "Press any key to exit."]


LOSS = ["Sorry, you were not able to break all the bricks :(",
        "Better luck next time.",
        "Thank you for playing! ",
        "Press any key to exit."]

class Brick(object):

    ''' This class is designed to initialize a graphics.py Rectangle as an attribute of Brick.
            - It keeps track of whether the Brick has been not hit, hit, or hit twice.
    '''

    def __init__(self, point1, point2):

        self.rect = Rectangle(point1, point2)
        self.p1 = point1
        self.p2 = point2
        self.hit = False
        self.remove = False

    def isHit(self):
        return self.hit

    def isRemoved(self):
        return self.remove

    def gotHit(self):
        self.hit = True

    def gotHit2(self):
        self.remove = True


def setup_window():
    ''' This function sets up and returns a graphics window as an object from graphics.py '''

    height = 700
    width = 1000

    win = GraphWin("BrickBreaker", width, height)
    win.setBackground("black")
    return win

def format_Text_array(win, strList):

    ''' This funtion takes in a list of strings and forms a list of graphics.py Test object 
            - The list is made to easily manipulate Text as a group
                - Sets text color, size, and location
        Returns the list of Text objects
    '''

    # Creates a Point object to center the text in the middle of the window
    x = win.getWidth()/2
    y = win.getHeight()/2
    center = Point(x,y)

    nextLine = 20          # The number of pixels below the next Text is centered at

    # Creates a list of Text objects and appends strList items centered at Point
    formattedText = []
    for string in strList:
        formattedText.append(Text(center, string))
        center.move(0,nextLine)

    # Formats text using Text methods to improve for user
    for text in formattedText:
        text.setSize(20)
        text.setTextColor("white")

    return formattedText

def draw_formatted_Text(win, formattedText):
    ''' This function takes in a list of Text objects and draws each item  into the graphics window '''

    for text in formattedText:
        text.draw(win)

def remove_formatted_Text(formattedText):

    for text in formattedText:
        text.undraw()

def init_bricks():
    ''' This function initializes all the specs of a brick
            - Function determines number of bricks and rows
            - each item in bricks is class Brick
            - Each spec is set as multiple of 4 to accomodate dx dy speed
            - Formats brick position and color
        Returns lisy of Brick
    '''

    bricks = []
    numBricks = 8       # number of bricks per row
    numRows = 4
    brickLength = 100
    brickHeight = 32
    xspace = 20                 #Space between bricks in same row
    yspace = brickHeight + 40   #space between bricks in row above or below

    #Creating two Points for class Rectangle
    #class Rectangle forms a rectangle using only topleft and bottomright corner
    x1 = 30
    y1 = 40
    x2 = x1 + brickLength
    y2 = y1 + brickHeight

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    #nested loop to append Brick along with both points to form Rectangle
    for i in range(numRows):
        for j in range(numBricks):
            bricks.append(Brick(p1, p2))

            # Points are cloned to avoid points recorded in Brick class to change here
            p1 = p1.clone()
            p2 = p2.clone()

            # Copy of previous point is moved to next Brick Points
            p1.move(brickLength + xspace, 0)
            p2.move(brickLength + xspace, 0)

        # resets Points to form new row
        y1 = y1 + yspace
        y2 = y2 + yspace

        p1 = Point(x1, y1)
        p2 = Point(x2, y2)

    # Set color for bricks
    for brick in bricks:
        brick.rect.setFill("red")

    return bricks

def draw_bricks(win, bricks):

    for brick in bricks:
        brick.rect.draw(win)

def init_quit_and_pause_instuctions_text(win):

    qcenter = Point(50, 10)
    qtext = Text(qcenter, "Press 'q' to quit")
    qtext.setTextColor("white")
    qtext.setSize(15)

    pcenter = Point(200, 10)
    ptext = Text(pcenter, "Press 'p' to pause")
    ptext.setTextColor("white")
    ptext.setSize(15)

    ptext.draw(win)
    qtext.draw(win)

def init_score_text(score, win):
    ''' Initializes a Text object displaying score to user
        Draws and returns Text object
    '''
    # initializes point on top right of graphics window
    x = win.getWidth()-100
    y = 10
    center = Point(x,y)

    scoreText = Text(center, f"Score: {score}")
    scoreText.setTextColor("white")
    scoreText.setSize(20)
    scoreText.draw(win)

    return scoreText

def add_score_text(score, win, scoreText):
    ''' This funtion reconfigures the score text
        setText automatically redraws the updated text to window
        Returns score to update it in main
    '''
    scoreText.setText(f"Score: {score}")

    return score

def init_lives_text(numChances, win):
    ''' Initializes a Text object displaying lives to user
        Draws and returns Text
    '''

    # initializes point in top right of screen, 100 pixels left to score
    x = win.getWidth() - 250
    y = 10
    center = Point(x,y)

    livesText = Text(center, f"Lives: {numChances}")
    livesText.setTextColor("white")
    livesText.setSize(20)

    livesText.draw(win)

    return livesText

def update_lives_text(numChances, win, livesText):
    ''' Reconfigures lives Text to current status
        Automatically redraws with .setText method
    '''

    livesText.setText(f"Lives: {numChances}")

def init_bar(winWidth, winHeight):

    #initializes bar to bottom of the window centered
    barlength = 80
    barheight = 20
    x1 = (winWidth/2) - (barlength/2)

    # initializes two points to use to form bar as Rectangle
    p1 = Point(x1, winHeight - barheight)
    p2 = Point(x1+barlength, winHeight)

    bar = Rectangle(p1,p2)

    bar.setFill("yellow") #sets bar color

    return bar

def init_ball(width, height, barheight):

    #initializes ball as graphics.py Circle just above bar
    radius = 10
    center = Point(width/2, height-barheight-radius)

    ball = Circle(center, radius)
    ball.setFill("white")
    return ball

def check_side_wall_collision(win, ball):
    rad = ball.getRadius()
    center = ball.getCenter()

    if(center.x - rad <= 0 or center.x + rad >= win.width):
        return True

    return False

def check_top_wall_collision(win, ball):
    rad = ball.getRadius()
    center = ball.getCenter()

    if(center.y - rad <= 0 ):
        return True

    return False

def check_right_left_brick_collision(ball, bricks):
    rad = ball.getRadius()
    ballX = ball.getCenter().getX()
    ballY = ball.getCenter().getY()

    # Check for left side
    for i in range(len(bricks)):
        if(not bricks[i].isRemoved()):
            if(ballY + rad >= bricks[i].p1.getY() and ballY - rad <= bricks[i].p2.getY() and
               (ballX + rad == bricks[i].p1.getX() or ballX - rad == bricks[i].p2.getX()) ):
                # Since conditions are met, returns True and index of that brick
                return True, i

    return False, None

def check_top_bottom_brick_collision(ball, bricks):
    rad = ball.getRadius()
    ballX = ball.getCenter().getX()
    ballY = ball.getCenter().getY()

    # Check for top side
    for i in range (len(bricks)):
        if(not bricks[i].isRemoved()):
            if(ballX + rad >= bricks[i].p1.getX() and ballX - rad <= bricks[i].p2.getX() and
               (ballY + rad == bricks[i].p1.getY() or ballY - rad == bricks[i].p2.getY()) ):
                #Since conditions are met, returns True and index of that brick
                return True, i

    return False, None

def check_bar_collision(ball, bar):
    rad = ball.getRadius()
    ballX = ball.getCenter().getX()
    ballY = ball.getCenter().getY()

    if(ballY + rad == bar.p1.getY() and ballX + rad >= bar.p1.getX() and ballX - rad <= bar.p2.getX() ):
        return True

def check_bottom_collision(win, ball):
    # Checks for collision with bottom window boundary
    rad = ball.getRadius()
    center = ball.getCenter()

    if(center.y + rad >= win.height):
        return True

    return False

def record_brick_collision(bricks, index):
    ''' Updates the indexed Brick to its updated condition '''

    # Since only drawn bricks are checked, there are only two possibilities for hit bricks
    if(bricks[index].isHit()):
        bricks[index].gotHit2()
    else:
        bricks[index].gotHit()

def change_brick_color(bricks, index):
    ''' Changes color of recently hit brick(using index) if was not removed  '''

    if(not bricks[index].isRemoved()):
        bricks[index].rect.setFill("blue")

def remove_bricks(bricks, index):
    ''' Removes recently hit brick(using index) if recorded to be removed '''

    if(bricks[index].isRemoved()):
        bricks[index].rect.undraw()

def check_all_removed(bricks):
    ''' Iterates through list of briks to see if any have not been removed; Returns boolean'''

    for brick in bricks:
        if(not brick.isRemoved()):
            return False

    return True

def setup_initial_game():
    barheight = 20
    numChances = 3
    score = 0

    win = setup_window()

    # Display instructions until user presses a key
    instructionsText = format_Text_array(win, INSTRUCTIONS)
    draw_formatted_Text(win, instructionsText)
    win.getKey()
    remove_formatted_Text(instructionsText)

    win.flush()

    # Initialize and draw bricks
    bricks = init_bricks()
    draw_bricks(win, bricks)

    # Initialize and draw ball
    ball = init_ball(win.width,  win.height, barheight)
    ball.draw(win)

    # Bar that keeps ball from touching bottom 
    bar = init_bar(win.width, win.height)
    bar.draw(win)

    # Print text to guide user options and updated game info
    init_quit_and_pause_instuctions_text(win)
    scoreText = init_score_text(score, win)
    livesText = init_lives_text(numChances, win)

    return win, bricks, bar, ball, scoreText, livesText

def check_all_collisions(win, ball, bricks, bar, dx, dy):
    ''' This function calls several functions to check ball collision with all game objects
        Returns:
            - updated direction the ball should be moved after collisions
            - Boolean of whether the ball hit the bottom of window
            - Boolean of whether there was a brick collision
                - The index of the brick or None if a brick was not hit
    '''

    #Check for window boundary collisions and change direction of ball if collision occurs
    bottomCollision = check_bottom_collision(win, ball)
    sideCollision = check_side_wall_collision(win, ball)
    topCollision = check_top_wall_collision(win, ball)

    if(sideCollision):
        dx *= -1
    if(topCollision):
        dy *= -1

    #Check for ball collisions with bricks, return which brick was colided with if applicable
    brickCollision = False
    index = None

    # index1 and index2 are used to see which brick was hit (added to handle corner collisions)
    brickTBcollision, index1 = check_top_bottom_brick_collision(ball, bricks)
    brickRLcollision, index2 = check_right_left_brick_collision(ball, bricks)

    if(brickTBcollision):
        dy *= -1
    if(brickRLcollision):
        dx *= -1

    if(brickRLcollision or brickTBcollision):
        brickCollision = True

        # One brick collision may have returned None if there was no corner collision
        # index variable with a value is taken to be the hit brick
        if(index1 or index1 == 0):
            index = index1
        else:
            index = index2

    #Check for ball collision with bar and change ball direction if so
    barCollision = check_bar_collision(ball, bar)
    if(barCollision):
        dy *= -1

    return dx, dy, bottomCollision, brickCollision, index

def reset_ball_and_bar(win, ball, bar, dx, dy, barheight):
    """ Resets game features ball and bar to middle after ball hit bottom window boundary
            - Returns new bar, ball, and updates ball direction
    """

    dy *= -1        #Changes ball direction to go up again
    ball.undraw()
    bar.undraw()
    bar = init_bar(win.width, win.height)
    bar.draw(win)
    ball = init_ball(win.width, win.height, barheight)
    ball.draw(win)
    ball.move(dx,dy)    # Moves ball one iteration to not be taken as a collision

    return ball, bar, dy

def main():

    #Initialize Variables
    dx = 1
    dy = 1
    userChar = None     #stores user input when playing game
    barMove = 40        # number of pixels the bottom bar moves by
    numChances = 3
    barheight = 20
    score = 0

    # setup grapics window and game features
    # also returns number of lives and score text for update later
    win, bricks, bar, ball, scoreText, livesText = setup_initial_game()

    # Control program flow of ball collisions, user-input, game status, and ball movement
    finished = False
    while(not finished and userChar != 'q' and numChances >= 0):

        # Use event waiting feature to see if there is user input 
        userChar = win.checkKey()
        if(userChar):

            if(userChar == '9'):
                bar.move(-barMove, 0)        # .move attribute takes in the x and y direction movement
            if(userChar == '0'):
                bar.move(barMove, 0)
            if(userChar == 'p'):
                pauseText = format_Text_array(win, PAUSE)
                draw_formatted_Text(win, pauseText)
                win.getKey()
                remove_formatted_Text(pauseText)


        # Check ball position against all objects and update ball direction if collision happens
        # The index returned refers to the index of the brick hit if applicable, None is returned if not
        dx, dy, bottomCollision, brickCollision, index = check_all_collisions(win, ball, bricks, bar, dx, dy)

        # Handles game restart and lost life when the ball hits the bottom window boundary 
        if(bottomCollision):
            numChances -= 1
            update_lives_text(numChances, win, livesText)

            if(numChances >= 0):
                ball, bar, dy = reset_ball_and_bar(win, ball, bar, dx, dy, barheight)

        # Handles the update of brick hit and then check to see whether bricks are still left
        if(brickCollision):

            record_brick_collision(bricks, index)       #Updates statues of  which brick was hit using index returned
            change_brick_color(bricks, index)           # Change color if first time brick was hit
            remove_bricks(bricks, index)                # Removes brick if this is second time hit
            score = add_score_text(score + 10, win, scoreText)

            # Check whether all bricks have been removed from grapics window and return boolean
            finished = check_all_removed(bricks)

        # Move ball to next position
        # At the end to make sure all user input and ball collisions were handled before moving the ball
        ball.move(dx, dy)


    # End game for user 
    ball.undraw()

    # checks whether all bricks were removed to print end 
    if(finished):
        gameEndText = format_Text_array(win, VICTORY)
    else:
        gameEndText = format_Text_array(win, LOSS)

    draw_formatted_Text(win, gameEndText)
    win.getKey()

    win.close()

if __name__ == "__main__":
    main()
