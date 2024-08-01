from tkinter import *

WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 540

CELL_EMPTY = 0
CELL_WALL = 1
CELL_EXIT = 2
CELL_COIN = 3
CELL_BOMB = 4
CELL_PLAYER = 5


score = 0
game_over = False
win = False


map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,5,0,1,3,0,0,1,3,0,0,0,0,0,0,0,0,0,3,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1],
    [1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,4,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,4,1,3,0,0,1,0,0,1],
    [1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,3,4,1,0,0,1,3,3,1,3,4,3,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,3,0,1],
    [1,0,0,1,0,0,0,3,1,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,3,0,1,0,0,0,0,3,0,0,0,0,3,0,0,1,0,0,1],
    [1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
]


def getPlayerPosition():
    global map
    playerRow = -1
    playerColumn = -1


    for rowIndex in range(len(map)) :
        if 5 in map[rowIndex] :
            playerRow = rowIndex
    for columnIndex in range(len(map[playerRow])):
        if map[playerRow][columnIndex] == 5 :
            playerColumn = columnIndex

    # TODO
    return  [playerRow, playerColumn]


def canGo(cell):
    global score,game_over
    if cell == CELL_EMPTY :
        result = True
    elif cell == CELL_WALL :
        result = False
    elif cell == CELL_EXIT :
        result = True
    elif cell == CELL_COIN :
        score += 10
        result = True
    elif cell == CELL_BOMB :
        result = True


    return result


def canGoRight():
    global map
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]
    
    rightCell = map[playerRow][playerColumn + 1]
    
    result = canGo(rightCell)

    return result


def canGoLeft():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    leftCell = map[playerRow][playerColumn - 1]
    result = canGo(leftCell)

    return result


def canGoUp():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    upCell = map[playerRow - 1][playerColumn]
    result = canGo(upCell)

    return result


def canGoDown():
    player = getPlayerPosition()

    playerRow = player[0]
    playerColumn = player[1]

    downCell = map[playerRow + 1][playerColumn]
    result = canGo(downCell)
    return result


def clickOnRigh(event):
    global map,game_over,win
    if canGoRight() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        if map[playerRow][playerColumn+1] == CELL_BOMB :
            game_over = True
        if map[playerRow][playerColumn+1] == CELL_EXIT :
            win = True

        map[playerRow][playerColumn+1] = 5
        map[playerRow][playerColumn] = 0
        
        game()


def clickOnLeft(event):
    global map,game_over,win
    if canGoLeft() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        if map[playerRow][playerColumn-1] == CELL_BOMB :
            game_over = True
        if map[playerRow][playerColumn+1] == CELL_EXIT :
            win = True

        map[playerRow][playerColumn-1] = 5
        map[playerRow][playerColumn] = 0
        
        game()
        
def clickOnUp(event):
    global map,game_over,win
    if canGoUp() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        if map[playerRow-1][playerColumn] == CELL_BOMB :
            game_over = True
        if map[playerRow][playerColumn+1] == CELL_EXIT :
            win = True

        map[playerRow-1][playerColumn] = 5
        map[playerRow][playerColumn] = 0
        
        game()    


def clickOnDown(event):
    global map,game_over,win
    if canGoDown() and not game_over:
        player = getPlayerPosition()

        playerRow = player[0]
        playerColumn = player[1]

        if map[playerRow+1][playerColumn] == CELL_BOMB :
            game_over = True
        if map[playerRow][playerColumn+1] == CELL_EXIT :
            win = True

        map[playerRow+1][playerColumn] = 5
        map[playerRow][playerColumn] = 0
        
        game()
      


def game() :
    global game_over,win
    if game_over :
        drawMap()
        canvas.create_text(700,200,fill="red",font="Times 20 italic bold",text="GAME OVER")
        a = Button(text="Play Again", bd="10", command=play_Again)
        a.place(relx=0.87, rely=0.5, anchor=CENTER)

    elif win :
        player_Win()
        canvas.create_text(300,250,fill="yellow",font="Times 30 italic bold",text="YOUR SCORE")
        canvas.create_text(300,300,fill="yellow",font="Times 30 italic bold",text=score)
        canvas.create_text(700,200,fill="green",font="Times 20 italic bold",text="YOU WIN")
        b = Button(text="Play Again", bd="10", command=play_Again)
        b.place(relx=0.87, rely=0.5, anchor=CENTER)

    else: 
        return drawMap()



def player_Win() :
    canvas.delete("all")
    global map,score

    win = False

    map = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]
    drawMap()


def play_Again() :
    
    canvas.delete("all")
    global map,game_over,score

    score=0
    game_over = False

    map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,5,0,1,4,0,3,1,0,0,3,0,0,0,0,0,0,0,3,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1],
    [1,4,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,4,1],
    [1,0,0,0,0,4,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,4,1,3,0,0,1,0,0,1],
    [1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,3,4,1,0,0,1,3,4,1,3,4,3,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,4,3,1],
    [1,0,0,1,0,0,0,3,1,0,0,0,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,3,0,1,0,0,0,0,3,0,0,0,0,3,0,0,1,4,4,1],
    [1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,3,1,0,3,0,1,0,0,3,0,0,1,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
    ]
    drawMap()


def drawMap():
    canvas.delete("all")
    global map,score
    canvas.create_image(250,265, image=bg)
    size = 30

    x = 15
    y = 15


    for array in map:
        for value in array:
            
            
            if value == CELL_WALL :
                canvas.create_image(x,y, image=wall)

            elif value == CELL_EXIT :
                canvas.create_image(x,y, image=exit)
           
            elif  value == CELL_COIN :
                canvas.create_image(x,y, image=coin)
           
            elif value == CELL_BOMB :
                canvas.create_image(x,y, image=bomb)

            elif value == CELL_PLAYER :
                canvas.create_image(x,y, image=player)
            
        
            x += size
            
        x = 15
        y += size

    canvas.create_text(700,80,fill="darkblue",font="Times 20 italic bold",text="Your Score")
    canvas.create_text(700,130,fill="darkblue",font="Times 20 italic bold",text=score)
    canvas.create_text(700,350,fill="darkblue",font="Times 15 italic bold",text="Collect The Coins")
    canvas.create_text(700,400,fill="red",font="Times 15 italic bold",text="Warning: ")
    canvas.create_text(700,450,fill="red",font="Times 10 italic bold",text="Becareful for the BOMB")

    



root = Tk() 
root.geometry( str(WINDOWS_WIDTH) +"x" + str(WINDOWS_HEIGHT))
canvas = Canvas(root)
 

wall = PhotoImage(file="boxCrate_double.png")
coin = PhotoImage(file="gold_1.png")
bomb = PhotoImage(file="bomb.png")
player = PhotoImage(file="femaleAdventurer_walk1.png")
exit = PhotoImage(file="signExit.png")
bg = PhotoImage(file="fae_BG.png")




canvas.pack(expand=True, fill='both')


root.bind("<Right>",clickOnRigh)
root.bind("<Left>",clickOnLeft)
root.bind("<Up>",clickOnUp)
root.bind("<Down>",clickOnDown)


drawMap()


root.mainloop()