# Author: Oluchukwu Catherine Obi-Njoku

# val_is_valid accepts the user's entry as a parameter
# returning 1 if valid and 0 if not

def val_is_valid(val):
   if val in {"1","2","3","4"}:
       return 1
   else:
       print("You can only input values: 1,2,3,4")
       return 0


# cell_is_valid accepts the game board, and the cell selected by the user, 
# verifies the existence and emptiness of the cell. 
# Returning valid position if valid and 0 if not

def cell_is_valid(board,pos):
    if pos != None and board[pos[0]][pos[1]] == 0:
        return pos
    else:
        return 0


# gen2by2Order accepts the row and col being modified by the user, 
# and returns a set of the corresponding 2 x 2 grouping it belongs to
# returning 1 if valid and 0 if not
def gen2by2Order(row,col):
    
    two_two_groups = [
        {(0,0), (0,1), (1,0), (1,1)},
        {(2,0), (2,1), (3,0), (3,1)},
        {(0,2), (0,3), (1,2), (1,3)},
        {(2,2), (2,3), (3,2), (3,3)}
    ]
    for i in two_two_groups:
        if (row,col) in i:
            return i
    return None


# valid2By2 accepts the user's entered number, game board, and played position,
# and checks if the number being inserted is valid in the 2 x 2 space
# returning 1 if valid and 0 if not

def valid2By2(num, board, pos):
    valid_cells = gen2by2Order(pos[0],pos[1])
    
    for i in valid_cells:
        if(num == board[i[0]][i[1]]):
            return 0
    return 1


# validRow accepts the user's entered number, game board, and played position row,
# and checks if the number being inserted is valid in the row space
# returning 1 if valid and 0 if not

def validRow(num, board, row):
    for i in board[row]:
        if(num == i):
            return 0
    return 1


# validCol accepts the user's entered number, game board, and played position col,
# and checks if the number being inserted is valid in the col space
# returning 1 if valid and 0 if not

def validCol(num, board, col):
    j = 0
    while j != 4:
        if num == board[j][col]:
            return 0
        j+=1
    return 1


# checkValidity accepts the user's entered number, game board, and played position,
# and combines validRow, validCol, and valid2By2 to determine the validity of the user's entry
# returning 1 if valid and 0 if not

def checkValidity(num, board, pos):
    if(validRow(num,board,pos[0]) and validCol(num,board,pos[1]) and valid2By2(num,board,pos)):
        return 1
    print("Your placing is incorrect")
    print("Your entry is similar to a value in either the same row, col, or 2 x 2 grouping")
    return 0


# updateBoard accepts the user's entered number, game board, and played position
# and updates the board with the played value at the given position

def updateBoard(num,board,pos):
    board[pos[0]][pos[1]] = num


# displayBoard accepts the game board, and displays it

def displayBoard(board):
    for i in board:
        print(i)

 
# gamePlay co-ordinates the game_play process, handling it from start to finish

def gamePlay(game_board, position_board, position_dict):
    
    in_progress = 'Y'
    total_score = 0
    
    while(in_progress == 'Y'):
        
        print("\n\nGame Board: \n")
        displayBoard(game_board)
        
        print("\nThese are the positions on the board \n")
        displayBoard(position_board)
        
        p = input("\nType in the number of the cell you want to modify: ")
        p_is_valid = cell_is_valid(game_board,position_dict.get(p))
        
        if(p_is_valid != 0):
            
            x = input("Enter the value you'd like to update the board with: ")
            if (val_is_valid(x) and checkValidity(int(x),game_board,p_is_valid)):
                updateBoard(int(x),game_board,p_is_valid)
                total_score += 1
            
        else:
            print("The cell you selected, either does not exist or is occupied")
            
        in_progress = input("Would you like to go on Y/N: ")
        
    print("\nThanks for playing, your score is ", total_score)
    print("If all cells are filled, the above is your perfect score\n")
        

def main():
    
    position_board_dict = {
        "1": [0,0], "2": [0,1], "3": [0,2], "4": [0,3],
        "5": [1,0], "6": [1,1], "7": [1,2], "8": [1,3],
        "9": [2,0], "10": [2,1], "11": [2,2], "12": [2,3],
        "13": [3,0], "14": [3,1], "15": [3,2], "16": [3,3],
    }
    
    position_board = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,16]]
    
    default_board = [[2,0,0,1],
                     [0,0,0,0],
                     [0,0,0,0],
                     [1,0,0,2]]
    
    gamePlay(default_board,position_board,position_board_dict)
    
    displayBoard(default_board)
    
if __name__=="__main__":
    main()