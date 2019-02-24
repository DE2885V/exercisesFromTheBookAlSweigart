#Крестики-нолики

import random

def drawBoard(board):
    # Эта функция выводит на экран игровое поле, клетки которого будут заполняться.

    # "board" - это списое из 10 строк, для прорисовки игрового поля (индекс 0 игнорируется).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Разрешение игроку ввести букву, которую он выбирает.
    # Возвращает список, в котором буква игрока - первый элемент, а буква компьютера  - второй.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете Х или О')
        letter = input().upper()

    # Первый элемент списка является буква игрока, вторым - буква компьютера.
    if letter == 'X':
        return  ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove (board, letter, move):
    board[move] = letter

def isWinner (bo, le):
    # Учитывая заполнение игрового поля и буквы игрока, эта функ. возвр. True,  если игрок выиграл.
    # Мы использ. "bo" вместо "board" и "le" вместо "letter", поэтому нам не нужно много печатать.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    # Создает копию игрового поля и возвращает его.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Возвращает True, если сделан ход в свободную клетку.
    return board[move] == ' '

def getPlayerMove(board):
    #Разрешение игроку сделать ход.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,  int(move)):
        print ('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Возвращает доступный ход, учитывая список сделаееых ходов и список заполненных клеток.
    # Возвращает значение None, если больше нет доступных ходов.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Это алгоритм для ИИ
    #
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверяет - победит ли игрок, сделав следю ход, и блокируем его.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Пробуем занять один из углов, если есть свободное.
    move = chooseRandomMoveFromList(board, [1, 3 , 7, 9])
    if move != None:
        return move

    # Пробуем занять центр, если он свободен.
    if isSpaceFree(board, 5):
        return 5

    # Делаем ход по одной стороне.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #
    for i in list(range(1, 10)):
        if isSpaceFree(board, i):
            return False
    return True


print ('Игра "Крестики-нолики"')

while True:
    # ...
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print ('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            #
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'

        else:
            #
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('y'):
        break