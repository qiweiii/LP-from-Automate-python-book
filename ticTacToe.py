#! python3

'''
In the Tic Tac Toe computer program the player chooses if they want to be X or O.
Who takes the first turn is randomly chosen.
Then the player and computer take turns making moves.
After the player or computer makes a move, the program checks if they won or caused a tie,
and then the game switches turns.
After the game is over, the program asks the player if they want to play again.
'''

# I think one reason why I did not complete the tic tac toe previously is because I did not
# plan -> draw flow chart -> write functions blocks -> put together

# First thing first, draw a flow chart diagram
# the website I learn tic tac toe: http://inventwithpython.com/chapter10.html

'''
The AI’s smarts for playing Tic Tac Toe will follow a simple algorithm.
An algorithm is a finite series of instructions to compute a result.
A single program can make use of several different algorithms.
An algorithm can be represented with a flow chart. The Tic Tac Toe AI’s algorithm will compute the best move to make,
as shown in Figure 10-4.

The AI’s algorithm will have the following steps:

1. First, see if there’s a move the computer can make that will win the game. If there is, take that move. Otherwise, go to step 2.

2. See if there’s a move the player can make that will cause the computer to lose the game.
If there is, move there to block the player. Otherwise, go to step 3.

3. Check if any of the corner spaces (spaces 1, 3, 7, or 9) are free. If so, move there. If no corner piece is free, then go to step 4.

4. Check if the center is free. If so, move there. If it isn’t, then go to step 5.

5. Move on any of the side pieces (spaces 2, 4, 6, or 8).
There are no more steps, because if the execution reaches step 5 the side spaces are the only spaces left.
'''

# The start of the program
import random # so i can call radiant() function


# Printing the board on the screen
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Letting the player be X or O
def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do u want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# Deciding who goes first
def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'


# Ask the player whether to play again
def playAgain():
    '''
    this function returns True if the player wants to play again, otherwise it returns False.
    '''
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# Place a mark on the Board
def makeMove(board,letter,position):
    board[position] = letter
    '''
    When a list value is passed for the board parameter,
    the function's local variable is really a copy of the reference to the list,
    not a copy of the list. But a copy of the reference still refers to the same list the original reference refers.
    So any changes to board in this function will also happen to the original list.
    Even though board is a local variable, the makeMove() function modifies the original list.
    '''


# Checking if the Player Has Won
def isWinner(bo, le):
    # board and letter, returns true if that player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom

    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side

    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle

    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side

    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal

    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


# Duplicate the board data
def getBoardCopy(board):
    # make a duplicate of board list and return the duplicate
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


# Check is space is free
def isSpaceFree(board, move):
    return board[move] == ' '


# Letting the player enter their move
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)): # make sure the move is valid
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


# AI
def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter ='O'
    else:
        playerLetter = 'X'

    # algorithm for AI
    # check if we can win in next move
    for i in range (1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree (copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # check if the player could win on their next move, and block them.
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # check if any of the corner spaces are free
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    # Try to take the center, if is it free
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])


# check if the Board is Full
def isBoardFull(board):
    for i in range (1,10):
        if isSpaceFree(board, i):
            return False
    return True


# Start of the Game
print('Welcome to Tic Tac Toe!')

while True:
    # reset the board
    theBoard = [' '] * 10

    # deciding who to go first
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    # Running the Player's Turn
    while gameIsPlaying:
        if turn == 'player':
            # player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! you have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # running computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie')
                        break
                else:
                        turn = 'player'


    # check if player want to play again
    if not playAgain():
        break
                
