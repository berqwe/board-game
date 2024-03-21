# ASSIGNMENT06, Comp 1405
# Bereket Ashebir Alemu 101282366

import pygame,random

# number of row and column
width = 7
height = 6

# square dimension
sq_dim = 50

# time for the time delay
time = 1100

screen = pygame.display.set_mode((width*sq_dim,height*sq_dim))
# colour variable
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)

# making a function for the board
def board():
    pygame.init()
    current_colour = white
    # visits each pixel and draws squares
    for i in range(0, width+1):
        for j in range(0, height+1):
            pygame.draw.rect(screen,current_colour,(i*sq_dim, j*sq_dim, sq_dim, sq_dim))
            pygame.display.update()
            # to alternate colours for the checkerboard	
            if current_colour == white:
               current_colour = black
            else:
               current_colour = white
    # draws the numbers on the board
    count = 1
    for row in range(0,height):
        for col in range(0,width):
            font = pygame.font.SysFont('arial',15)
            text = font.render(str(count),True,(255,0,0))
            screen.blit(text,((col*sq_dim),(row*sq_dim)))
            # count incremented by one in each loop
            count = count + 1
            pygame.display.update()
# function that covers the player previous positions
def cover_up(x,y):
    # if the last two digits of the x and y coordinates are the same then
    # white circles are drawn in white squares otherwise black circles are drawn.
    # The x and y coordinates are added to 100 so that if x,y are two digit numbers(like 25,75)
    # then the x,y mod 100 won't give the last two digit
    u = (x + 100)%100
    v = (y + 100)%100
    if u != v:
        pygame.draw.circle(screen, black, (x, y), 15)
    else:
        pygame.draw.circle(screen, white, (x, y), 15)
    return x,y


board()
def main():
    #x,y postions of player 1
    p1x = sq_dim/2
    p1y = sq_dim/2

    #x,y postions of player 2
    p2x = sq_dim/2
    p2y = sq_dim/2

    # draws the circles
    pygame.draw.circle(screen, blue, (p1x, p1y), 15)
    pygame.draw.circle(screen, green, (p2x, p2y), 15)
    pygame.display.update()
    pygame.time.delay(time)

    flag = True
    while flag:

        # player 1 plays first
        player = 1

        # if condition to switch players
        if player ==1:
            # two sided dices
            dice1 = random.randint(1,2)
            dice2 = random.randint(1,2)

            # adds the dice1 + dice2 and prints it
            Total_dice = dice1 + dice2
            print("Dice for player 1:",Total_dice)
            print()

            # covers the circle 1's position
            cover_up(p1x,p1y)

            # calculates the new x-ordinates based the number of moves for player 1
            p1x =  p1x + sq_dim*Total_dice

            # breaks the loop if it reaches the last square and prints the winner
            if (p1y >= 275) and (p1x >= 325):
                # ensures the player is on the last square and not beyond
                p1y = 275
                p1x = 325

                # draws the circle in the last square
                pygame.draw.circle(screen, blue, (p1x, p1y), 15)
                pygame.display.update()
                flag = False
                print("player 1 wins")
                break

            # ensures the circle doesn't go beyond the edge
            if p1x > 325:
                # calculates by how many square units is the circle
                # off the edge
                off_edge_sq = ((p1x - 325)/sq_dim)
                # moves to the next row
                p1y = p1y + sq_dim
                # calculates x coordinate in the new row
                p1x = (sq_dim*off_edge_sq - sq_dim/2)


        # draws player1's new position
        pygame.draw.circle(screen, blue, (p1x, p1y), 15)
        pygame.display.update()
        pygame.time.delay(time)

        #switches to player 2
        player = 2

        if player == 2:
            # covers the circle 2's position
            cover_up(p2x,p2y)

            # two 2-sided dices
            dice1 = random.randint(1,2)
            dice2 = random.randint(1,2)

            # adds the dice1 + dice2 and prints it
            Total_dice = dice1 + dice2
            print("Dice for player 2:",Total_dice)
            print()
            # calculates the new x-ordinates based the number of moves for player 2
            p2x = p2x + sq_dim*Total_dice

            # breaks the loop if it reaches the last square and prints the winner
            if p2y >= 275 and p2x >= 325:
                # ensures the player is on the last square and not beyond it
                p2y = 275
                p2x = 325

                # draws the cicle in the last square
                pygame.draw.circle(screen, green, (p2x, p2y), 15)
                pygame.display.update()
                # to break the loop
                flag = False
                # prints the winner
                print("player 2 wins")
                break
            # ensures the circle doesn't go beyond the edge
            if p2x > 325:
                # calculates by how many square units is the circle
                # off the edge
                off_edge_sq = ((p2x - 325)/sq_dim)
                # moves to the next row below
                p2y = p2y + sq_dim
                # calculates x coordinate in the new row
                p2x = (sq_dim*off_edge_sq - sq_dim/2)

        # draws player2's new position
        pygame.draw.circle(screen, green, (p2x, p2y), 15)
        pygame.display.update()
        pygame.time.delay(time)

        # switches to player 1
        player = 1
main()

# keeps the window opened until user close it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
