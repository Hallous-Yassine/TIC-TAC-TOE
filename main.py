import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    x , y = 0 , 0
    for i in range(13):
        for j in range(25):
            if (i % 4 == 0 and j % 8 == 0):
                print('+' , end = '')
            elif (j % 8 == 0):
                print('|' , end = '')
            elif (i % 4 == 0):
                print('-' , end = '')
            elif ( j % 4 == 0 and i % 2 == 0 ):
                if (y >= len(board[x])):
                    x+=1
                    y=0
                print(board[x][y] , end = '')
                y += 1
            else:
                print(' ' , end = '')
        print('\n')
    
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        x = input("Enter Your Move: ")
        try:
            x = int(x)
            row = (x - 1) // 3
            col = (x - 1) % 3
            if(x < 1 or x > 9 or not isinstance(board[row][col],int)):
                print("Error : Invalid Input")
                continue
            else:
                board[row][col] = 'o'
                display_board(board)
                break
        except:
            print("Error : Invalid Input")
    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list = []
    for i in range(len(board)):
        for j in range(len(board)):
            if(isinstance(board[i][j],int)):
                list.append((i,j))
    return list

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if(board[0][i] == board[1][i] == board[2][i] == sign):
            return True
        if(board[i][0] == board[i][1] == board[i][2] == sign):
            return True
        if(board[0][0] == board[1][1] == board[2][2] == sign):
            return True
        if(board[2][0] == board[1][1] == board[0][2] == sign):
            return True
    return False
        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = random.choice(make_list_of_free_fields(board))
    board[move[0]][move[1]] = 'x'
    display_board(board)

board = [
    [1,2,3],
    [4,'x',6],
    [7,8,9],
]


display_board(board)
while True:
    enter_move(board)
    if (victory_for(board, 'o')):
        print("You won!")
        exit()
    draw_move(board)
    if (victory_for(board, 'x')):
        print("Computer Won!")
        exit()
